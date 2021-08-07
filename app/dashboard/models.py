# models for dashboard bp

last_date = (
    """SELECT
           MAX(date_local) AS last_date
       FROM 
           gps_tracker_gps_data
    """
)

speed = (
    """SELECT
           timestamp_utc_ms,
           speed
       FROM 
           gps_tracker_gps_data
       WHERE
           date_local = date%s
    """
)

map_data = (
    """SELECT 
           timestamp_utc_ms,
           latitude,
           longitude,
           speed
       FROM
           gps_tracker_gps_data
       WHERE
           date_local = date%s
    """
)

truck_turnaround_time = (
    """SELECT
           hour,
           current_truck_turnaround_time AS curr_ttt,
           improved_truck_turnaround_time AS impr_ttt
       FROM
           truck_turnaround_time
    """
)