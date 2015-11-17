#v1.0.1 - Initial Release
#Central Heating Controller

This central heating controller requires WiringPi, WiringPi for Python and RPi.GPIO to be installed.

I use a script called at reboot by cron to start the script in a new Screen so that output is available in real time.

sudo screen -r heating

command to run at reboot (I have mine in crontab).

screen -d -m -S heating bash -c "sudo python /home/pi/GitRepo/centralheating/default.py"

change path to wherever you have this installed to.

The schedule is held in resources/python/schedule.py

The min temp is set in default.py.

It utilises 2 Raspberry PI's, one runs the Central Heating controller and the other controls the relay. 
The program includes  2 leds to display current heating status, and one button for manual override.

Currently the WebApp is accessed via apache and symlinking index.php and resources folder to apaches default home.

Future features & to do.....

- External Sensor and weather dependant programming.
- WebApp front end (IN PROGRESS).
- QT Gui.
- Android app.
- Install Script
