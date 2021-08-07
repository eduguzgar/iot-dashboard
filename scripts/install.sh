#!/bin/bash

# ask for root
sudo echo "" > /dev/null

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

source ${DIR}/.env

export PGPASSWORD=$DB_PASS

# create required project folders
echo "INFO: CREATING PROJECT FOLDERS."

# create data folder
mkdir ${DIR}/data

# create log folders
mkdir ${DIR}/app/log
mkdir ${DIR}/database/log
mkdir ${DIR}/comm_protocol/log

# set up the entire project database
echo "INFO: SETTING UP THE DATABASE."

# set up role and database
sudo -u postgres psql -f ${DIR}/database/config/role.sql
sudo -u postgres psql -f ${DIR}/database/config/database.sql

# create required functions
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/config/functions.sql

# create tables schema
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/config/schema.sql

# load tables
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -vdir="${DIR}/data" -f ${DIR}/database/data_shipping.psql
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/truck_turnaround_time.sql
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/gps_geofence_zones.sql

# execute scheduled postgresql tasks and log only stderr
cron_lines="*/5 * * * * PGPASSWORD='"$PGPASSWORD"' psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/truck_turnaround_time.sql 2>> ${DIR}/database/log/truck_turnaround_time.txt"

if ! crontab -l | grep -Fxq "$cron_lines"; then
    (crontab -u $USER -l; echo "$cron_lines" ) | crontab -u $USER - 
    echo "INFO: INSTALLING NEW CRONTABS."
else
    echo "INFO: CRONTABS ARE UP TO DATE, SKIPPING."
fi