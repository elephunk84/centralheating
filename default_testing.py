#v1.0.3.4
#!/bin/python

day_temp=16.999
night_temp=19.999
ips=['192.168.0.25', '192.168.0.26']

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
templog='/home/pi/GitRepo/centralheating/resources/database/templog_' + date + '.db'
datalog='/home/pi/GitRepo/centralheating/resources/database/datalog.db'
__builtin__.callback = ''
__builtin__.chon=''
ch_status=''
time_now=''

def ping_ip():
    global occupied
    for ip in ips:
        response = os.system("ping -c 1 " + ip + " > /dev/null")
        if response == 1:
            response2 = os.system("ping -c 1 " + ip + " > /dev/null")
            if response2 == 1:
                response3 = os.system("ping -c 1 " + ip + " > /dev/null")
                if response3 == 1:
					occupied='NO'
					return
                else:
                    occupied='YES'
                    return
        else:
            occupied='YES'
            return
		    
def log_temperature(temp):
    with sqlite3.connect(templog) as tempconn:
        curs=tempconn.cursor()
        tablename='temps'
        tablecheck='create table if not exists ' + tablename + '(timestamp DATETIME, temp NUMERIC, occupied text, advance text);'
        curs.execute(tablecheck)
        curs.execute("INSERT INTO temps values (?, ?, ?, ?);",  (temp_time, temp, occupied, manual_override) )
        tempconn.commit()
    f=open('resources/temp', 'w')
    f.write(str(temp))
    f.close()

def log_status_change():
    with sqlite3.connect(datalog) as dataconn:
        curs=dataconn.cursor()
        tablename='status'
        tablecheck='create table if not exists ' + tablename + '(timestamp DATETIME, occupied text, advance text);'
        curs.execute(tablecheck)
        curs.execute("INSERT INTO status values (?, ?, ?);",  (temp_time, occupied, ch_status) )
        dataconn.commit()
        
def display_data():
    print ""
    print "Templog...."
    print "--------------------------------------"
    conn=sqlite3.connect(templog)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM temps ORDER BY ROWID DESC LIMIT 10;"):
        print str(row[0])+"		"+str(row[1])+"		"+str(row[2])+"		"+str(row[3])
    conn.close()
    print ""
    print "Datalog...."
    print "TIME		   OCCUPIED		STATUS"
    print "--------------------------------------"
    conn=sqlite3.connect(datalog)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM status ORDER BY ROWID DESC LIMIT 10;"):
        print str(row[0])+"		"+str(row[1])+"		"+str(row[2])
    conn.close()

def read_db():
    conn=sqlite3.connect(templog)
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
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    status = ('ON') in open('resources/webstatus').read()
    if ( status == True ):
        pass
    else:
        wiringpi.digitalWrite(0, 1)
        wiringpi.digitalWrite(2, 0)
        f=open('resources/webstatus', 'w')
        f.write('ON')
        f.close()
        subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/on.sh"])
        log_status_change()

def off():
    print "Central Heating is " + ch_status + "...."
    print "--------------------------------------"
    status = ('OFF') in open('resources/webstatus').read()
    if ( status == True ):
        pass
    else:
        wiringpi.digitalWrite(0, 0)
        wiringpi.digitalWrite(2, 1)
        f=open('resources/webstatus', 'w')
        f.write('OFF')
        f.close()
        subprocess.call(["ssh", "pi@192.168.0.129", "sh /home/pi/off.sh"])
        log_status_change()

def clear_screen():
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print

def logic():
    clear_screen()
    global ch_status
    global temp
    global set_temp
    global temp_time
    global manual_override
    now = datetime.datetime.now()
    now_today=str(now.strftime("%H:%M"))    
    temp_time = now.strftime("%H:%M:%S")
    devicelist = glob.glob('/sys/bus/w1/devices/28-*')
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
    set_day()
    ping_ip()
    print "--------------------------------------"
    print "Is anybody home?...." + occupied 
    if __builtin__.chstatus == "ON" and (str(temp) <= str(set_temp)) and ( occupied == 'YES'):     
        ch_status='ON'
    else:
        ch_status='OFF'
    if (ch_status == 'ON') and ('ON' in open('resources/status').read()):
        manual_override='ON'
        print "Manual Override is " + manual_override + "...."
        off()
        clean_up()
    elif (ch_status == 'ON'):
        manual_override='OFF'
        print "Manual Override is " + manual_override + "...."
        on()
        clean_up()
    elif (ch_status == 'OFF') and ('ON' in open('resources/status').read()):
        manual_override='ON'
        print "Manual Override is " + manual_override + "...."
        on()
        clean_up()
    else:
        manual_override='OFF'
        print "Manual Override is " + manual_override + "...."
        off()
        clean_up()

GPIO.add_event_detect(22, GPIO.FALLING, callback=my_callback, bouncetime=300)

if __name__ == "__main__":
    while True:
        logic()
        next_run()
        time.sleep(3)
        log_temperature(temp)
