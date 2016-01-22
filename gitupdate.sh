#!/bin/bash
cd /home/pi/GitRepo/centralheating
echo "Which branch have you been editing testing/main???"
main='main'
testing='testing'
read version
echo $version
if [ "$version" = "$testing" ]; then 
    echo "Copying testing to main...." 
    cp default_testing.py default.py;
fi
if [ "$version" = "$main" ]; then
    echo "Copying main to testing...."
    cp default.py default_testing.py;
fi
echo "Adding files to git...." 
git add --all
echo "git Commit comment ="
read comment
git commit -m \"$comment\"
echo "git Push...."
git push origin master > /dev/null
