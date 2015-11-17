#!/bin/python
import os
import sys
import subprocess
lib_path = os.path.abspath(os.path.join('/home/pi/GitRepo/centralheating/', 'lib'))
sys.path.append(lib_path)

import __builtin__
import time
import datetime
import sqlite3
import glob
import socket
import wiringpi2 as wiringpi
import RPi.GPIO as GPIO
import resources.python.schedule as schedule
from resources.python.schedule import *
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.pinMode(2, 1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
hostname=socket.gethostname()
dbname='/home/pi/GitRepo/centralheating/resources/templog.db'
now=datetime.datetime.now()
today=now.strftime("%A")
time_now=time.strftime("%H:%M", time.localtime(time.time()))
logtime=time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
temp_min='25'
__builtin__.callback = ''
global run_status
run_status=''

def log_temperature(temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO temps values (?, ?);",  (logtime, temp) )
    conn.commit()
    conn.close()

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
    wiringpi.digitalWrite(0, 0)
    wiringpi.digitalWrite(2, 1)
    print "Central Heating is ON...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/on.sh"])
    f=open('resources/webstatus', 'w')
    f.write('ON')
    f.close()

def off():
    wiringpi.digitalWrite(0, 1)
    wiringpi.digitalWrite(2, 0)
    print "Central Heating is OFF ...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/off.sh"])
    f=open('resources/webstatus', 'w')
    f.write('OFF')
    f.close()

def schedule_check():
    if (time_now in open('resources/run_schedule').read()):     
        run_status='ON'
        temp_check()
    else:
        run_status='OFF'

def temp_check():
    if (run_status == 'ON'):
        if (str(temp) <= str(temp_min)):
            run_temp='ON'
            print run_temp
    else:
        run_temp='OFF'


def logic():
    global ch_status
    global temp
    global run_status
    global run_temp
    run_temp='OFF'
    status=str(open('resources/status').read())
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    w1devicefile = devicelist[0] + '/w1_slave'
    fileobj = open(w1devicefile,'r')
    lines = fileobj.readlines()
    fileobj.close()
    tempstr= lines[1][-6:-1]
    tempvalue=float(tempstr)/1000
    temp=tempvalue
    f=open('resources/temp', 'w')
    f.write(str(temp))
    f.close()
    print "--------------------------------------"
    print "Current Temperature is...."
    print temp
    log_temperature(temp)
    set_day()
    schedule_check()
    print str(status)
    if str(status) == 'ON' and run_temp == 'OFF':
        print 'ON'
    elif run_temp == 'OFF':
        print 'OFF'
    else:
        pass
GPIO.add_event_detect(22, GPIO.FALLING, callback=my_callback, bouncetime=300)

if __name__ == "__main__":
    while True:
        logic()
        time.sleep(2)
