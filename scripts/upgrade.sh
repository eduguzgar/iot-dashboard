#!/bin/bash

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

# set output console colors
RED=$(tput setaf 9) BLUE=$(tput setaf 14)
NC=$(tput sgr0)

# set message output states
INFO="[${BLUE}INFO${NC}] - "
ERROR="[${RED}ERROR${NC}] - "

# check if venv is active and is the same project folder
venv=$(printenv | grep VIRTUAL_ENV)

if [ -z "$venv" ]; then
    printf "\n${ERROR}VENV IS NOT ACTIVE, PLEASE ACTIVATE IT AND TRY AGAIN\n\n"
    exit 1
else
    venv=${venv#"VIRTUAL_ENV="}
    if [[ $venv != $DIR* ]]; then
        printf "\n${ERROR}VENV IS ACTIVE, BUT IT DOES NOT BELONG TO THIS PROJECT\n\n"
        exit 1
    fi
fi

# if venv is active, perform upgrade
printf "${INFO}PERFORMING PIP UPGRADE, PLEASE CHECK FOR ERRORS\n\n"

pip freeze > ${DIR}/requirements.txt
sleep 4
sed -i 's/==/>=/' ${DIR}/requirements.txt

pip install -r requirements.txt --upgrade
sleep 4
pip freeze > ${DIR}/requirements.txt