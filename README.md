# centralheating
Iain's Central Heating Control


This central heating controller requires WiringPi and WiringPi for Python to be installed.

I use a script called at reboot by cron to start the script in a new Screen so that output is available in real time.\n
sudo screen -r heating\n

command to run at reboot.\n
screen -d -m -S heating bash -c "sudo python /home/pi/GitRepo/centralheating/default.py"\n
change path to wherever you have installed it to.\n

The schedule is held in resources/python/schedule.py

The min and max temps are set in default.py.


Future features & to do.....

- WebApp front end
- QT Gui
- Android app
