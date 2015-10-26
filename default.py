#!/bin/python
import os
import sys

lib_path = os.path.abspath(os.path.join('/home/pi/GitRepo/centralheating/', 'lib'))
sys.path.append(lib_path)

import time
import datetime
import pytz
import sqlite3
import glob
import socket
from resources.python import monitor
import wiringpi2 as wiringpi
from resources.python.schedule import *
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1) # sets GPIO 25 to input
wiringpi.pinMode(2, 1) # sets GPIO 24 to output

hostname=socket.gethostname()
dbname='/home/pi/GitRepo/centralheating/resources/python/templog_' + str(hostname) + '.db'

def localtime():
    time_now=time.ctime()
    return time_now

def log_temperature(temperature):
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print time_now
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO temps values (?, ?);",  (time_now, temperature) )
    conn.commit()
    conn.close()

def display_data():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT * FROM temps"):
        print str(row[0])+"	"+str(row[1])
    conn.close()

def get_temp(devicefile):
    try:
        fileobj = open(devicefile,'r')
        lines = fileobj.readlines()
        fileobj.close()
    except:
        return None
    status = lines[0][-4:-1]
    if status=="YES":
        tempstr= lines[1][-6:-1]
        tempvalue=float(tempstr)/1000
        global temperature
        temperature=tempvalue
        print temperature
        log_temperature(temperature)
        time.sleep(10)
        return    
    else:
        print "There was an error."
        return None

def monitor():
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    w1devicefile = devicelist[0] + '/w1_slave'
    temperature = get_temp(w1devicefile)
    if temperature != None:
        print "temperature="+str(temperature)
    else:
        get_temp(w1devicefile)

def read_db():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("SELECT temp FROM temps;")
    conn.commit()
    temperature=curs.fetchone()

def control():
    while True:
        monitor()
        if (temperature >= 22) and (temperature <=25):
            wiringpi.digitalWrite(0, 1)
            wiringpi.digitalWrite(2, 0)
        else:
            wiringpi.digitalWrite(0, 0)
            wiringpi.digitalWrite(2, 1)


if __name__ == "__main__":
    control()
