#!/bin/bash
cd /home/pi/GitRepo/centralheating/resources
status=$(cat 1hradvance)
timenow=$(date +"%T")
if [ "$status" = "" ]; then
    hour1=$(date +"%H")
    hour2=$((hour1 + 1))
    if [ "$hour2" = "24" ]; then
        hour2="00"
    fi
    timethen=${hour2}:$(date +"%M")
    echo "ON till ${timethen}" > ./1hradvance
else
    echo "" > ./1hradvance
fi
