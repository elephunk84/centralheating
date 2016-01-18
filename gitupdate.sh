#!/bin/bash
cd /home/pi/GitRepo/centralheating
echo "Adding files to git...." 
git add --all
echo "git Commit comment ="
read comment
git commit -m \"$comment\"
echo "git Push...."
git push origin master
