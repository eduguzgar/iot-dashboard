DO $$
BEGIN

DELETE FROM truck_turnaround_time;

ALTER SEQUENCE truck_turnaround_time_id_seq
    RESTART WITH 1;

INSERT INTO truck_turnaround_time (hour, hour_ms, current_truck_turnaround_time, improved_truck_turnaround_time)
SELECT
    to_timestamp(extract(hour FROM release_entry_date)::text, 'hh24')::time,
    extract(epoch FROM (to_timestamp(extract(hour FROM release_entry_date)::text, 'hh24')::time)) * 1000,
    avg(extract(epoch FROM (release_date - release_entry_date)) / 60),
    avg(extract(epoch FROM (release_date - release_entry_date)) / 60) - random_between (20, 30)
FROM
    data_shipping
WHERE -- trash data filtered, maybe truck plate not read at exit
    release_date >= release_entry_date
    AND extract(epoch FROM (release_date - release_entry_date)) / 60 < 1200
GROUP BY
    to_timestamp(extract(hour FROM release_entry_date)::text, 'hh24')::time;

END;
$$ LANGUAGE 'plpgsql';

