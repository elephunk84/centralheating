#v1.0.1 - Initial Release
#!/bin/python

day_temp=16.999
night_temp=19.999
iains_ip='192.168.0.25'
eloras_ip='192.168.0.26'

import os
import sys
import subprocess
lib_path = os.path.abspath(os.path.join('/home/pi/GitRepo/centralheating/', 'lib'))
sys.path.append(lib_path)
import math
import __builtin__
import time
import datetime
import sqlite3
import glob
import socket
import wiringpi2 as wiringpi
import RPi.GPIO as GPIO
import resources.python.schedule as schedule
from resources.python import monitor
from resources.python.schedule import *
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.pinMode(2, 1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
hostname=socket.gethostname()
now = datetime.datetime.now()
date = now.strftime("%a-%d-%B-%Y")
dbname='/home/pi/GitRepo/centralheating/resources/database/templog_' + date + '.db'
__builtin__.callback = ''
__builtin__.chon=''
ch_status=''
time_now=''
global occupied

def ping_ip():
	global occupied
	ips=[iains_ip, eloras_ip]
	for ip in ips:
		response = os.system("ping -c 1 " + ip + " > /dev/null")
		if response == 0:
                        occupied='YES'
                        return
		else:
                        occupied='NO'



def log_temperature(temp):
    with sqlite3.connect(dbname) as conn:
        curs=conn.cursor()
        tablename='temps'
        tablecheck='create table if not exists ' + tablename + '(timestamp DATETIME, temp NUMERIC);'
        curs.execute(tablecheck)
        curs.execute("INSERT INTO temps values (?, ?);",  (time_now, temp) )
        conn.commit()
    f=open('resources/temp', 'w')
    f.write(str(temp))
    f.close()

def templog(temp1, temp2):
    conn=sqlite.connect(maindb)
    curs=conn.cursor()
    curs.execute()    

def display_data():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM temps ORDER BY ROWID DESC LIMIT 10;"):
        print str(row[0])+"	"+str(row[1])
    conn.close()

def read_db():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("SELECT temp FROM temps;")
    conn.commit()
    temperature=curs.fetchone()

def my_callback(channel):
    if ('ON' in open('resources/webstatus').read()):
        f=open('resources/status', 'w')
        f.write('')
        f.close()
    else:
        f=open('resources/status', 'w')
        f.write('ON')
        f.close()

def on():
    wiringpi.digitalWrite(0, 1)
    wiringpi.digitalWrite(2, 0)
    f=open('resources/webstatus', 'w')
    f.write('ON')
    f.close()
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/on.sh"])

def off():
    wiringpi.digitalWrite(0, 0)
    wiringpi.digitalWrite(2, 1)
    f=open('resources/webstatus', 'w')
    f.write('OFF')
    f.close()
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/off.sh"])

def logic():
    global ch_status
    global temp
    global set_temp
    now = datetime.datetime.now()
    now_today=str(now.strftime("%H:%M"))    
    devicelist = glob.glob('/sys/bus/w1/devices/28-0314634e50ff')
    w1devicefile = devicelist[0] + '/w1_slave'
    fileobj = open(w1devicefile,'r')
    lines = fileobj.readlines()
    fileobj.close()
    tempstr= lines[1][-6:-1]
    tempvalue=float(tempstr)/1000
    temp=tempvalue
    if str(now_today) < str("17:00"):
        set_temp=str(day_temp)
    else:
        set_temp=str(night_temp)
    temp_set=math.ceil(float(set_temp))
    print "--------------------------------------"
    print "Current Temperature is " + str(temp) + "...."
    print "The Temperature is set to " + str(temp_set) + "...."
    print "--------------------------------------"
    set_day()
    log_temperature(temp)
    ping_ip()
    print "--------------------------------------"
    print "Is anybody home?... " + occupied
    if __builtin__.chstatus == "ON" and (str(temp) <= str(set_temp)) and ( occupied == 'YES'):     
        ch_status='ON'
    else:
        ch_status='OFF'
    if (ch_status == 'ON') and ('ON' in open('resources/status').read()):
        ch_status='OFF'
        manual_override='ON'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        off()
    elif (ch_status == 'ON') and (occupied == 'YES'):
        manual_override='OFF'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        if 'ON' in (open('resources/holiday').read()):
            print "Holiday Mode Enabled...."
            off()
        else:
            on()
    elif (ch_status == 'OFF') and ('ON' in open('resources/status').read()):
        manual_override='ON'
        ch_status='ON'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        if 'ON' in (open('resources/holiday').read()):
            print "Holiday Mode Enabled...."
            off()
        else:
            on()
    else:
        manual_override='OFF'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        off()

GPIO.add_event_detect(22, GPIO.FALLING, callback=my_callback, bouncetime=300)

if __name__ == "__main__":
    while True:
        logic()
        next_run()
        clean_up()
        time.sleep(3)

