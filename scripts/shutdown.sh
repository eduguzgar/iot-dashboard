#!/bin/bash

# ask for root
sudo echo "" > /dev/null
if ! sudo -n true 2>/dev/null; then exit 1; fi

DIR="$( dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )")"

# set output console colors
RED=$(tput setaf 9) BLUE=$(tput setaf 14)
NC=$(tput sgr0)

# set message output states
INFO="[${BLUE}INFO${NC}] - "
ERROR="[${RED}ERROR${NC}] - "

# kill flask instance running
printf "${INFO}SHUTTING DOWN FLASK INSTANCE\n"
sudo pkill -f "${DIR}/.*/flask run"

# kill all comm protocols running
printf "${INFO}SHUTTING DOWN COMMUNICATION PROTOCOLS\n"

# kill Micktrack MT821/825 comm protocol
printf "${INFO}SHUTTING DOWN MT82X COMM PROTOCOL\n"
mt82x_all=($(pgrep -f "python -m comm_protocol.mt82x"))

# save only PIDs for this project
declare -a mt82x
for pid in "${mt82x_all[@]}"; do
	proc=$(sudo ls -l /proc/$pid/cwd)
	cwd=$(echo $proc | awk '{print $NF}')
	if [[ $cwd == \'*\' ]]; then
		cwd="${cwd#?}"; cwd="${cwd%?}"
	fi
	if [ "$cwd" = "$DIR" ]; then
		mt82x+=$pid
	fi
done

for pid in "${mt82x[@]}"; do
	sudo kill $pid
done