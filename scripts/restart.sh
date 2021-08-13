#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

"${DIR}/shutdown.sh"
sleep 4
echo ""
"${DIR}/start.sh"