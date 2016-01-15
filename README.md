#v1.0.3 - Central Heating Controller

This is a central heating controller that uses 2 Raspberry Pi's to control my boiler. You can set it to run on a schedule, if the temperature isnt warm enough, and also if anybody is home ( pings network to find mobile phones connected to wifi, phone must have static ip and wifi on, i use tasker to make sure wifi is on when i get home).
 
Currently the WebApp is accessed via apache and symlinking index.php and resources folder to apaches default home.

Future features & to do.....

- External Sensor and weather dependant programming.
- WebApp front end (IN PROGRESS).
- QT Gui.
- Android app.
- Install Script
