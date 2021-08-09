/* Create databases for the different use cases */
CREATE EXTENSION IF NOT EXISTS dblink;

/* Use case example */
DO $do$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'dev') THEN
    PERFORM dblink_exec('dbname=' || current_database(), 'create database dev with owner = dev');
    ELSE
    RAISE NOTICE 'database already exists';
    END IF;
END
$do$;

