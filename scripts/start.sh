#!/bin/bash

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

cd $DIR

TODAY=$(LANG=en_us_88591;date -u)
TODAY_YMD=`date -u --date="$TODAY" +'%Y%m%d'`

# check if venv is active and is the same project folder
venv=$(printenv | grep VIRTUAL_ENV)

if [ -z "$venv" ]; then
    echo "ERROR: VENV IS NOT ACTIVE, PLEASE ACTIVATE IT AND TRY AGAIN."
    exit 1
else
    venv=${venv#"VIRTUAL_ENV="}
    if [[ $venv == $DIR* ]]; then
        echo "INFO: VENV IS ACTIVE"
    else
        echo "ERROR: VENV IS ACTIVE, BUT IT DOES NOT BELONG TO THIS PROJECT"
        exit 1
    fi
fi

source .env

# start flask instance
source app/.env

# add current date when app started
if [ ! -f app/log/log_${TODAY_YMD}.txt ]; then
    echo -e "INFO: INIT ON ${TODAY}:\n" >> app/log/log_${TODAY_YMD}.txt
else
    echo -e "\n\nINFO: INIT ON ${TODAY}:\n" >> app/log/log_${TODAY_YMD}.txt
fi

echo "INFO: STARTING FLASK INSTANCE."
nohup flask run --host=0.0.0.0 >> app/log/log_${TODAY_YMD}.txt 2>&1 &

# start comm protocols
source comm_protocol/.env
echo "INFO: STARTING COMMUNITACION PROTOCOL MODULES."

# mt82x
echo "INFO: STARTING MT82X COMM PROTOCOL."
source comm_protocol/.mt82x
nohup python -m comm_protocol.mt82x >> comm_protocol/log/log_${TODAY_YMD}.txt 2>&1 &