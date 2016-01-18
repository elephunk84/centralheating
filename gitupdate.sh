#!/bin/bash
cd /home/pi/GitRepo/centralheating
git add --all
read comment
git commit -m \"$comment\"
git push origin master
