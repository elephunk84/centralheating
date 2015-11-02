#!/bin/python
import os
import sys

lib_path = os.path.abspath(os.path.join('/home/pi/GitRepo/centralheating/', 'lib'))
sys.path.append(lib_path)

import __builtin__
import time
import datetime
import sqlite3
import glob
import socket
from resources.python import monitor
import wiringpi2 as wiringpi
import resources.python.schedule as schedule
from resources.python.schedule import *
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.pinMode(2, 1)
hostname=socket.gethostname()
maindb='/home/pi/GitRepo/centralheating/resources/python/templog.db'
dbname='/home/pi/GitRepo/centralheating/resources/python/templog_' + str(hostname) + '.db'
now=datetime.datetime.now()
today=now.strftime("%A")
time_now=time.strftime("%H:%M", time.localtime(time.time()))
temp_max=25
temp_min=20
__builtin__.status="ON"
ch_on=""
ch_off=""

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

def control():
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    w1devicefile = devicelist[0] + '/w1_slave'
    fileobj = open(w1devicefile,'r')
    lines = fileobj.readlines()
    fileobj.close()
    tempstr= lines[1][-6:-1]
    tempvalue=float(tempstr)/1000
    temp=tempvalue
    temp1=temp
    print "Current Temperature is...."
    print  temp
    log_temperature(temp)
    set_day()
    if (temp <= temp_min) and (time_now in open('run_schedule').read()):
        wiringpi.digitalWrite(0, 0)
        wiringpi.digitalWrite(2, 1)
        print "Central Heating Running...."
        print "--------------------------------------"
    else:
        wiringpi.digitalWrite(0, 1)
        wiringpi.digitalWrite(2, 0)
        print "Cental Heating Off...."
        print "--------------------------------------"


if __name__ == "__main__":
    while True:
        control()
        time.sleep(30)
