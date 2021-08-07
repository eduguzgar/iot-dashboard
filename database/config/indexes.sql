CREATE INDEX IF NOT EXISTS current_truck_turnaround_time_truck_turnaround_time_idx ON truck_turnaround_time(current_truck_turnaround_time);
CREATE INDEX IF NOT EXISTS improved_truck_turnaround_time_truck_turnaround_time_idx ON truck_turnaround_time(improved_truck_turnaround_time);

CREATE INDEX IF NOT EXISTS imei_gps_tracker_gps_data_idx ON gps_tracker_gps_data(imei);
CREATE INDEX IF NOT EXISTS timestamp_utc_gps_tracker_gps_data_idx ON gps_tracker_gps_data(timestamp_utc);
CREATE INDEX IF NOT EXISTS date_local_gps_tracker_gps_data_idx ON gps_tracker_gps_data(date_local);
CREATE INDEX IF NOT EXISTS latitude_gps_tracker_gps_data_idx ON gps_tracker_gps_data(latitude);
CREATE INDEX IF NOT EXISTS longitude_gps_tracker_gps_data_idx ON gps_tracker_gps_data(longitude);
CREATE INDEX IF NOT EXISTS speed_gps_tracker_gps_data_idx ON gps_tracker_gps_data(speed);

CREATE INDEX IF NOT EXISTS imei_gps_tracker_cell_data_idx ON gps_tracker_cell_data(imei);
CREATE INDEX IF NOT EXISTS timestamp_utc_gps_tracker_cell_data_idx ON gps_tracker_cell_data(timestamp_utc);
CREATE INDEX IF NOT EXISTS date_local_gps_tracker_cell_data_idx ON gps_tracker_cell_data(date_local);
CREATE INDEX IF NOT EXISTS cell_id_gps_tracker_cell_data_idx ON gps_tracker_cell_data(cell_id);
CREATE INDEX IF NOT EXISTS pcid_gps_tracker_cell_data_idx ON gps_tracker_cell_data(pcid);

CREATE INDEX IF NOT EXISTS imei_gps_geofence_entries_idx ON gps_geofence_entries(imei);
CREATE INDEX IF NOT EXISTS old_zone_gps_geofence_entries_idx ON gps_geofence_entries(old_zone);
CREATE INDEX IF NOT EXISTS new_zone_gps_geofence_entries_idx ON gps_geofence_entries(new_zone);