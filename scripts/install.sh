#!/bin/bash

# ask for root
sudo echo "" > /dev/null

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

# set output console colors
RED=$(tput setaf 9) BLUE=$(tput setaf 14)
NC=$(tput sgr0)

# set message output states
INFO="[${BLUE}INFO${NC}] - "
ERROR="[${RED}ERROR${NC}] - "

source ${DIR}/.env

export PGPASSWORD=$DB_PASS

# prompt for importing data tables
fill_tables=false
while true
do
    read -r -p "Do you want to import data tables? [Y/N] " input

    case $input in
        [yY][eE][sS]|[yY])
            fill_tables=true
            break
            ;;
        [nN][oO]|[nN])
            break
                ;;
        *)
        echo "Invalid input"
        ;;
    esac
done
echo ""

# create required project folders
printf "${INFO}CREATING PROJECT FOLDERS\n"

# create data folder
mkdir ${DIR}/data

# create log folders
mkdir ${DIR}/app/log
mkdir ${DIR}/database/log
mkdir ${DIR}/comm_protocol/log

# set up the entire project database
printf "\n${INFO}SETTING UP THE DATABASE\n"

# set up role and database
sudo -u postgres psql -f ${DIR}/database/role.sql
sudo -u postgres psql -f ${DIR}/database/database.sql

# create required functions
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/functions.sql

# create tables schema
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/schema.sql

# import data tables
if [ "$fill_tables" = true ] ; then
    psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -vdir="${DIR}/data" -f ${DIR}/database/import_data.psql
fi

# load tables
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/tables/truck_turnaround_time.sql
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/tables/gps_geofence_zones.sql

# create indexes
psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/indexes.sql

# execute scheduled postgresql tasks and log only stderr
cron_lines="*/5 * * * * PGPASSWORD='"$PGPASSWORD"' psql $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f ${DIR}/database/tables/truck_turnaround_time.sql 2>> ${DIR}/database/log/truck_turnaround_time.log"

if ! crontab -l | grep -Fxq "$cron_lines"; then
    printf "\n${INFO}INSTALLING CRONTABS\n"
    (crontab -u $USER -l; echo "$cron_lines" ) | crontab -u $USER - 
else
    printf "\n${INFO}CRONTABS ALREADY INSTALLED, SKIPPING\n"
fi
