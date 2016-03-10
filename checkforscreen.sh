#!/bin/bash

TEST=$(screen -ls | grep -c heating)
NOTFOUND="0"
FOUND="1"
echo $TEST
echo "Found = " $FOUND "Not Found = " $NOTFOUND
case "$NOTFOUND" in 
 "$TEST" )
  echo "Not found, Starting..."
  screen -dm -S heating bash -c "sudo python /home/pi/GitRepo/centralheating/default.py"
  ;;
esac
