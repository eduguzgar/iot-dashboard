CREATE TABLE IF NOT EXISTS data_shipping (
    id serial PRIMARY KEY,
    creation_date timestamp NOT NULL,
    container varchar(256),
    operation varchar(256) GENERATED ALWAYS AS (
        CASE 
            WHEN release_state = 'EMPTY' AND acceptance_state = 'FULL' THEN 'EXPORT'
            WHEN release_state = 'FULL' AND acceptance_state = 'EMPTY' THEN 'IMPORT'
            ELSE 'MOVE'
        END) STORED,
    release_truck_plate varchar(256),
    acceptance_truck_plate varchar(256),
    closing_time_valid_date timestamp,
    release_expiration_date timestamp,
    acceptance_expiration_date timestamp,
    iso_type varchar(50),
    release_state varchar(50),
    acceptance_state varchar(50),
    release_company_name varchar(256),
    acceptance_company_name varchar(256),
    unloading_berth_request_number bigint,
    loading_berth_request_number bigint,
    unloading_vessel_name varchar(256),
    loading_vessel_name varchar(256),
    load_date timestamp,
    discharge_date timestamp,
    release_estimated_date timestamp,
    release_proposed_date timestamp,
    release_real_date timestamp,
    acceptance_estimated_date timestamp,
    acceptance_proposed_date timestamp,
    acceptance_real_date timestamp,
    release_entry_date timestamp,
    release_exit_date timestamp,
    release_date timestamp
);

CREATE TABLE IF NOT EXISTS truck_turnaround_time (
    id serial PRIMARY KEY,
    hour time without time zone UNIQUE,
    hour_ms int UNIQUE,
    current_truck_turnaround_time double precision,
    improved_truck_turnaround_time double precision
);

CREATE TABLE IF NOT EXISTS gps_tracker_cell_data (
    id serial PRIMARY KEY,
    head varchar(256),
    mode smallint,
    imei bigint,
    ip varchar(45),
    port int,
    data_type varchar(256),
    timestamp_utc timestamp without time zone,
    timestamp_utc_ms bigint,
    date_local date,
    mnc smallint,
    cell_id bigint,
    lac integer,
    mcc smallint,
    pcid smallint,
    event_id smallint,
    voltage double precision,
    sequence_number smallint
);

CREATE TABLE IF NOT EXISTS gps_tracker_gps_data (
    id serial PRIMARY KEY,
    head varchar(256),
    mode smallint,
    imei bigint,
    ip varchar(45),
    port int,
    data_type varchar(256),
    satellite_n integer,
    timestamp_utc timestamp without time zone,
    timestamp_utc_ms bigint,
    date_local date,
    latitude double precision,
    longitude double precision,
    speed double precision,
    heading double precision,
    event_id smallint,
    voltage double precision,
    sequence_number smallint
);

CREATE TABLE IF NOT EXISTS gps_geofence_zones (
    id int PRIMARY KEY,
    name varchar(256),
    polygon polygon
);

CREATE TABLE IF NOT EXISTS gps_geofence_entries (
    id serial PRIMARY KEY,
    imei bigint,
    timestamp_utc timestamp without time zone,
    latitude double precision,
    longitude double precision,
    speed double precision,
    old_zone int,
    new_zone int,
    mode_change_success boolean,
    gps_tracker_gps_data_id bigint,
    CONSTRAINT gps_tracker_gps_data_id_fk
    FOREIGN KEY(gps_tracker_gps_data_id)
    REFERENCES gps_tracker_gps_data(id),
    CONSTRAINT gps_geofence_zones_id_old_zone_fk
    FOREIGN KEY(old_zone)
    REFERENCES gps_geofence_zones(id),
    CONSTRAINT gps_geofence_zones_id_new_zone_fk
    FOREIGN KEY(new_zone)
    REFERENCES gps_geofence_zones(id)
);

