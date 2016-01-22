#!/bin/bash
cd /home/pi/GitRepo/centralheating/resources
status=$(cat status)
echo $status
if [ $status = "ON" ]; then
    echo "OFF" > ./status
else
    echo "ON" > ./status
fi
