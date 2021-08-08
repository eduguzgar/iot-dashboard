#!/bin/bash

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

# set output console colors
RED=$(tput setaf 9) BLUE=$(tput setaf 14)
NC=$(tput sgr0)

# set message output states
INFO="[${BLUE}INFO${NC}] - "
ERROR="[${RED}ERROR${NC}] - "

cd $DIR

TODAY=$(LANG=en_us_88591;date -u)
TODAY_YMD=`date -u --date="$TODAY" +'%Y%m%d'`

# check if venv is active and is the same project folder
venv=$(printenv | grep VIRTUAL_ENV)

if [ -z "$venv" ]; then
    printf "${ERROR}VENV IS NOT ACTIVE, PLEASE ACTIVATE IT AND TRY AGAIN\n"
    exit 1
else
    venv=${venv#"VIRTUAL_ENV="}
    if [[ $venv != $DIR* ]]; then
        printf "${ERROR}VENV IS ACTIVE, BUT IT DOES NOT BELONG TO THIS PROJECT\n"
        exit 1
    fi
fi

source .env

# start flask instance
source app/.env

# add current date when app started
if [ ! -f app/log/log_${TODAY_YMD}.log ]; then
    echo -e "[INFO] - Init on ${TODAY}:\n" >> app/log/log_${TODAY_YMD}.log
else
    echo -e "\n\n[INFO] - Init on ${TODAY}:\n" >> app/log/log_${TODAY_YMD}.log
fi

printf "${INFO}STARTING FLASK INSTANCE\n"
nohup flask run --host=0.0.0.0 >> app/log/log_${TODAY_YMD}.log 2>&1 &

# start comm protocols
source comm_protocol/.env
printf "${INFO}STARTING COMMUNICATION PROTOCOL MODULES\n"

# mt82x
printf "${INFO}STARTING MT82X COMM PROTOCOL\n"
source comm_protocol/.mt82x
nohup python -m comm_protocol.mt82x >> comm_protocol/log/log_${TODAY_YMD}.log 2>&1 &