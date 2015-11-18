#!/bin/bash
cd /home/pi/GitRepo/centralheating
screen -dm -S heating bash -c "sudo python default.py"
