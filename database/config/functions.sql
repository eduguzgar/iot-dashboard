CREATE OR REPLACE FUNCTION random_between (low int, high int)
RETURNS int
AS $$
BEGIN
    RETURN floor(random() * (high - low + 1) + low);
END;
$$
LANGUAGE 'plpgsql'
STRICT;

CREATE OR REPLACE FUNCTION table_is_empty(table_name character varying)
RETURNS bool
AS $$
DECLARE
v int;
BEGIN
    EXECUTE 'SELECT 1 WHERE EXISTS( SELECT 1 FROM ' || quote_ident(table_name) || ' ) '
        INTO v;
    IF v THEN return false; ELSE return true; END IF;
END;
$$ 
LANGUAGE 'plpgsql'
STRICT;