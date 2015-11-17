
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
from resources.python import monitor
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
temp_min=19.999
__builtin__.callback = ''
ch_status='OFF'

def log_temperature(temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO temps values (?, ?);",  (time_now, temp) )
    conn.commit()
    conn.close()

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
    if ('ON' in open('resources/status').read()):
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
    f=open('resources/webstatus', 'w')
    f.write('ON')
    f.close()
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/on.sh"])

def off():
    wiringpi.digitalWrite(0, 1)
    wiringpi.digitalWrite(2, 0)
    f=open('resources/webstatus', 'w')
    f.write('OFF')
    f.close()
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/off.sh"])

def logic():
    global ch_status
    global temp
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    w1devicefile = devicelist[0] + '/w1_slave'
    fileobj = open(w1devicefile,'r')
    lines = fileobj.readlines()
    fileobj.close()
    tempstr= lines[1][-6:-1]
    tempvalue=float(tempstr)/1000
    temp=tempvalue
    print "--------------------------------------"
    print "Current Temperature is...."
    print temp
    log_temperature(temp)
    set_day()
    if (time_now in open('resources/run_schedule').read()) and (temp <= temp_min):     
        ch_status='ON'
    else:
        ch_status='OFF'
    if (ch_status == 'ON') and ('ON' in open('resources/status').read()):
        ch_status='OFF'
        manual_override='ON'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        off()
    elif ch_status == 'ON':
        manual_override='OFF'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
        on()
    elif (ch_status == 'OFF') and ('ON' in open('resources/status').read()):
        manual_override='ON'
        ch_status='ON'
        print "--------------------------------------"
        print "Manual Override is " + manual_override + "...."
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
        time.sleep(2)

