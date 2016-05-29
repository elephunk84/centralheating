#!/bin/bash
cd /home/pi/GitRepo/centralheating/resources
status=$(cat summer)
echo $status
if [ $status = "ON" ]; then
    echo "OFF" > ./summer
else
    echo "ON" > ./summer
fi
