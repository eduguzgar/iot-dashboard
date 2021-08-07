# all required queries for comm protocol

insert_gps_data = (
    """INSERT INTO gps_tracker_gps_data (
           head,
           mode,
           imei,
           ip,
           port,
           data_type,
           satellite_n,
           timestamp_utc,
           timestamp_utc_ms,
           date_local,
           latitude,
           longitude,
           speed,
           heading,
           event_id,
           voltage,
           sequence_number
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        returning id
    """
)

insert_cell_data = (
    """INSERT INTO gps_tracker_cell_data (
           head,
           mode,
           imei,
           ip,
           port,
           data_type,
           timestamp_utc,
           timestamp_utc_ms,
           date_local,
           mnc,
           cell_id,
           lac,
           mcc,
           pcid,
           event_id,
           voltage,
           sequence_number
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        returning id
    """
)

insert_geofence_entry = (
    """INSERT INTO gps_geofence_entries (
           imei,
           timestamp_utc,
           latitude,
           longitude,
           speed,
           old_zone,
           new_zone,
           mode_change_success,
           gps_tracker_gps_data_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        returning id
    """
)

select_old_zone = (
    """SELECT
           new_zone
       FROM 
           gps_geofence_entries
       WHERE
           imei = %s
       ORDER BY id DESC
       FETCH FIRST ROW ONLY
    """
)
