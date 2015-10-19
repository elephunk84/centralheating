#!/usr/bin/env python

import sqlite3
import os
import time
import glob
import socket
import datetime

speriod=(15*60)-1
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
        print tempvalue
        temperature=tempvalue
        log_temperature(temperature)
        time.sleep(3)
            
    else:
        print "There was an error."
        return None

def main():
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    if devicelist=='':
        return None
    else:
        w1devicefile = devicelist[0] + '/w1_slave'
    while True:
        temperature = get_temp(w1devicefile)
        if temperature != None:
            print "temperature="+str(temperature)
        else:
            get_temp(w1devicefile)

if __name__=="__main__":
    main()




