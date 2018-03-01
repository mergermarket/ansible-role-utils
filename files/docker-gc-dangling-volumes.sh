#!/bin/bash

set -e

LOG_FILE=/var/log/docker-gc-dangling-volumes.log

echo -n "cleaning up dangling volumes..." >> $LOG_FILE

docker volume ls -qf dangling=true | xargs -r docker volume rm >> $LOG_FILE

echo done >> $LOG_FILE
