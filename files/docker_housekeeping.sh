#!/bin/bash

set -e

# Check to see if the user-data has run 
if [ -f /var/log/user-data-has-run ] ; then
    docker ps -aq | xargs docker container stop || echo "Dont fail"
    docker system prune -af --filter 'until=72h'
    docker volume prune -f
    docker network prune -f
    docker system df
fi
