import os
from datetime import datetime
import pytz

# socket
from .udp_server_multi_client import UDPServerMultiClient

# database
from .database.database import DatabaseConnectionPool, Database
from .database import (
    DB_HOST, 
    DB_PORT, 
    DB_NAME, 
    DB_USER, 
    DB_PASS,
    DB_POOL_MINCONN,
    DB_POOL_MAXCONN
)

# required queries
from .database.queries import (
    insert_gps_data,
    insert_cell_data,
    insert_geofence_entry,
    select_old_zone,
)

# geofencing
from gps.geofence import point_in_polygon

# geofence polygons
from gps.constants import (
    POLY_1,
    POLY_2,
    POLY_3,
    POLY_4,
    ZONE_1,
    ZONE_2,
    ZONE_3,
    ZONE_4,
    ZONE_OUTTER
)

# socket config
HOST = os.environ["HOST"]
PORT = int(os.environ["PORT"])
BUFF_SIZE = int(os.environ["BUFF_SIZE"])
DESC = os.environ["DESC"]

# MT82x comands
PWR_SAVING_MODE_CMD  = "mode,5,5#"  # 5 minutes (GPS Sleep)
MID_ACTIVE_MODE_CMD  = "mode,6,20#" # 20 seconds
HIGH_ACTIVE_MODE_CMD = "mode,6,10#" # 10 seconds

# init database connection pool
DB_POOL = DatabaseConnectionPool(
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASS,
    DB_POOL_MINCONN,
    DB_POOL_MAXCONN
)
DB_POOL.init()

# create both timezone objects
OLD_TIMEZONE = pytz.timezone("UTC")
NEW_TIMEZONE = pytz.timezone("Europe/Madrid")

def parse_data(data):
    """Parse all received data in a list"""

    items = []
    separators = [";", "+", ","]
    data_len = len(data)

    i = 0
    while i < data_len:
        item = ""
        while i < data_len and data[i] not in separators:
            item += data[i]
            i += 1
        items.append(item)
        i += 1

    # get data type
    data_types = ["R0", "R1", "R12", "R13", "R2", "R3", "RH", "RC"]

    try:
        data_type = items[3]
    except IndexError:
        data_type = None

    # this means that the message is actually a cmd response
    if data_type not in data_types:
        data_type = None

    return items, data_type


def add_data(items, data_type, client_address):
    """Add data enrichment to keep generic tables in our database.

    The SQL table 'gps_tracker_gps_data' may contain data parsed from
    devices from different brands, where the data sent differs between
    devices and does not follow the same format.

    In addition, Micktrak(MT) devices when connected to LTE send the P-CID,
    but when connected to GSM the devices skip this field.

    This function should be implemented in any other comm protocol as well.
    """

    if data_type == "R2":       # if GSM cell data append None
        items.insert(9, None)

    items[11] = int(items[11]) / 1000  # voltage

    items.insert(3, client_address[0])  # add ip address
    items.insert(4, client_address[1])  # add port

    if data_type == "R0":
        items[7] = datetime.strptime(items[7], "%y%m%d%H%M%S")
        epoch = datetime.utcfromtimestamp(0)
        items.insert(8, (items[7] - epoch).total_seconds() * 1000)
        items.insert(9, OLD_TIMEZONE.localize(items[7]).astimezone(NEW_TIMEZONE).date())

    if data_type == "R2" or data_type == "R3":
        items[6] = datetime.strptime(items[6], "%y%m%d%H%M%S")
        epoch = datetime.utcfromtimestamp(0)
        items.insert(7, (items[6] - epoch).total_seconds() * 1000)
        items.insert(8, OLD_TIMEZONE.localize(items[6]).astimezone(NEW_TIMEZONE).date())

    return items


def insert_data(items, data_type, db):
    """Insert parsed data in database.
    Tables:
        - gps_tracker_gps_data
        - gps_tracker_cell_data
    """

    # gps data
    if data_type == "R0":
        record_to_insert = (
            items[0],   # head
            items[1],   # mode
            items[2],   # imei
            items[3],   # ip
            items[4],   # port
            items[5],   # data type
            items[6],   # satellite n
            items[7],   # timestamp utc
            items[8],   # timestamp utc ms
            items[9],   # date_local
            items[10],  # latitude
            items[11],  # longitude
            items[12],  # speed
            items[13],  # heading
            items[14],  # event id
            items[15],  # voltage
            items[16],  # sequence number
        )
        query = insert_gps_data

        rowid = db.execute_query_write(query, record_to_insert)
        print("GPS Data added entry id={}".format(rowid), flush=True)
    # cell data
    elif data_type == "R2" or data_type == "R3":
        record_to_insert = (
            items[0],   # head
            items[1],   # mode
            items[2],   # imei
            items[3],   # ip
            items[4],   # port
            items[5],   # data type
            items[6],   # timestamp utc
            items[7],   # timestamp utc ms
            items[8],   # date_local
            items[9],   # mnc
            items[10],  # cell_id
            items[11],  # lac
            items[12],  # mcc
            items[13],  # pcid
            items[14],  # event id
            items[15],  # voltage
            items[16],  # sequence number
        )
        query = insert_cell_data

        rowid = db.execute_query_write(query, record_to_insert)
        print("Cell Data added entry id={}".format(rowid), flush=True)

    return rowid


def add_geofence_entry(items, rowid, old_zone, new_zone, mode_change_success, db):
    """Register geofence entry info in gps_geofence_entries table"""
    record_to_insert = (
        items[2],               # imei
        items[7],               # timestamp utc
        items[10],              # latitude
        items[11],              # longitude
        items[12],              # speed
        old_zone,               # old zone
        new_zone,               # new zone
        mode_change_success,    # mode change success
        rowid,                  # gps_tracker_gps_data_id
    )
    query = insert_geofence_entry

    rowid = db.execute_query_write(query, record_to_insert)
    print("GPS Geofence added entry id={}".format(rowid), flush=True)


def get_old_zone(imei, db):
    """Get the last zone used by the GPS tracker"""
    query = select_old_zone
    old_zone = db.execute_query_read(query, imei)

    # get the old_zone out
    if not old_zone:
        old_zone = None
    else:
        old_zone = old_zone[0][0]

    return old_zone


def check_geofence(items, rowid, sock, client_address, db):
    """Function to check for changes in geofence zones"""
    satellite_n = items[6]
    lat = float(items[10])
    lon = float(items[11])

    # false position, don't let it change the zone
    if satellite_n == 0 or (lat == 0 and lon == 0):
        return

    imei = items[2]

    old_zone = get_old_zone(imei, db)   # get old zone

    if point_in_polygon(lat, lon, POLY_4) is True:              # we are in ZONE 4
        if old_zone != ZONE_4:                                  # check if we changed zone
            if old_zone == ZONE_OUTTER or old_zone is None:
                command = HIGH_ACTIVE_MODE_CMD
                sock.sendto(command.encode(), client_address)   # send command to device
            add_geofence_entry(items, rowid, old_zone, ZONE_4, None, db)

    elif point_in_polygon(lat, lon, POLY_3) is True:            # we are in ZONE 3
        if old_zone != ZONE_3:                                  # check if we changed zone
            if old_zone == ZONE_OUTTER or old_zone is None:
                command = HIGH_ACTIVE_MODE_CMD
                sock.sendto(command.encode(), client_address)   # send command to device
            add_geofence_entry(items, rowid, old_zone, ZONE_3, None, db)

    elif point_in_polygon(lat, lon, POLY_1) is True:            # we are in ZONE 1
        if old_zone != ZONE_1:                                  # check if we changed zone
            if old_zone == ZONE_OUTTER or old_zone is None:
                command = HIGH_ACTIVE_MODE_CMD
                sock.sendto(command.encode(), client_address)   # send command to device
            add_geofence_entry(items, rowid, old_zone, ZONE_1, None, db)

    elif point_in_polygon(lat, lon, POLY_2) is True:            # we are in ZONE 2
        if old_zone != ZONE_2:                                  # check if we changed zone
            if old_zone == ZONE_OUTTER or old_zone is None:
                command = HIGH_ACTIVE_MODE_CMD
                sock.sendto(command.encode(), client_address)   # send command to device
            add_geofence_entry(items, rowid, old_zone, ZONE_2, None, db)

    else:                                                       # we are in OUTTER ZONE
        if old_zone != ZONE_OUTTER:                             # check if we changed zone
            command = PWR_SAVING_MODE_CMD
            sock.sendto(command.encode(), client_address)       # send command to device
            add_geofence_entry(items, rowid, old_zone, ZONE_OUTTER, None, db)


def handler(data, sock, client_address):
    """Handler function to pass the UDP socket"""

    # database
    db = Database(DB_POOL)
    db.open()

    # insert data
    items, data_type = parse_data(data)

    # if this is true, then we parsed a cmd response, so return
    if data_type is None:
        print(items[0], flush=True)
        return

    items = add_data(items, data_type, client_address)
    rowid = insert_data(items, data_type, db)

    ### DEBUG ONLY
    for item in items:
        print(item, flush=True)
    ###

    if data_type == "R0":
        check_geofence(items, rowid, sock, client_address, db)


def main():
    udp_server_multi_client = UDPServerMultiClient(HOST, PORT, BUFF_SIZE, handler, DESC)
    udp_server_multi_client.configure_server()
    udp_server_multi_client.wait_for_client()


if __name__ == "__main__":
    main()
