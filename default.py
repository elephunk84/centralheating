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
import resources.python.schedule as schedule
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.pinMode(2, 1)
hostname=socket.gethostname()
maindb='/home/pi/GitRepo/centralheating/resources/python/templog.db'
dbname='/home/pi/GitRepo/centralheating/resources/python/templog_' + str(hostname) + '.db'
now=datetime.datetime.now()
today=now.strftime("%A")
time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
temp_max=25
temp_min=20

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
    while True:
        devicelist = glob.glob('/sys/bus/w1/devices/28*')
        w1devicefile = devicelist[0] + '/w1_slave'
        fileobj = open(w1devicefile,'r')
        lines = fileobj.readlines()
        fileobj.close()
        tempstr= lines[1][-6:-1]
        tempvalue=float(tempstr)/1000
        temp=tempvalue
        temp1=temp
        print temp
        log_temperature(temp)
        print_day()
        if (temp >= temp_min) and (temp <= temp_max):
            wiringpi.digitalWrite(0, 1)
            wiringpi.digitalWrite(2, 0)
            time.sleep(30)
        else:
            wiringpi.digitalWrite(0, 0)
            wiringpi.digitalWrite(2, 1)
            time.sleep(30)


if __name__ == "__main__":
    control()
