/* Create dev role */
DO $do$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = 'dev') THEN
    CREATE ROLE dev WITH LOGIN PASSWORD 'this-really-needs-to-be-changed';
    ELSE
    RAISE NOTICE 'role already exists';
END IF;
END
$do$;