#!/bin/bash

# ask for root
sudo echo "" > /dev/null

DIR="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ))"

# set output console colors
RED=$(tput setaf 9) BLUE=$(tput setaf 14) PURPLE=$(tput setaf 13)
NC=$(tput sgr0)

# set message output states
INFO="[${BLUE}INFO${NC}] - "
ERROR="[${RED}ERROR${NC}] - "

printf "\n${INFO}APPLICATION SERVICES STATUS, IF EMPTY ${PURPLE}MAYBE${NC} NOT RUNNING\n"
echo ""
sudo ps aux | grep "flask run\|-m comm_protocol.mt82x" | grep -v grep
echo ""