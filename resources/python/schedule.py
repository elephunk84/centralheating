#!/usr/bin/python
import json
import datetime
import sys
import timefiller as timefiller
import __builtin__
from pprint import pprint
import os
import copy
global now
now = datetime.datetime.now()
global today
today=now.strftime("%A")
global hour
hour=now.strftime("%H")
global minute
minute=now.strftime("%M")
global timer
timer=""
Monday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]

          ]  
Tuesday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "22:00", "23:30"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]

          ]  
Wednesday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]

          ]  
Thursday = [

          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]

          ]  
Friday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]

          ]  
Saturday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]
          ]  
Sunday = [
          [1, "04:00", "05:15"],
          [2, "15:48", "08:15"],
          [3, "15:49", "00:15"],
          [4, "15:50", "00:15"],
          [5, "15:40", "11:42"],
          [6, "15:41", "00:00"],
          [7, "15:24", "15:15"],
          [8, "15:25", "20:00"],
          [9, "15:26", "11:30"],
          [0, "15:27", "00:00"]
          ]  

def set_day():
    global timer
    if today == "Monday":
        timer=list(Monday)
        run_timer()
    elif today == "Tuesday":
        timer=list(Tuesday)
        run_timer(Tuesday)
    elif today == "Wednesday":
        timer=list(Wednesday)
        run_timer(Wednesday)
    elif today == "Thursday":
        timer=list(Thursday)
        run_timer()
    elif today == "Friday":
        timer=list(Friday)
        run_timer()
    elif today == "Saturday":
        timer=list(Saturday)
        run_timer()
    elif today == "Sunday":
        timer=list(Sunday)
        run_timer()
    else:
        dumpclean(Week)

def run_timer(mylist):
    global timenow
    timenow=hour + ":" + minute
    print "Time now is.....\n" +  today, timenow
    global status
    global on
    global off
    print timer
    search = timenow
    print timenow
    for sublist in timer:
        if sublist[1] == search:
            __builtin__.status="ON"
            print "Status: ON"
        else:
            __builtin__.status="OFF"

def print_timer():
    for n in timer:
        print n
    print timer[3]

if __name__ == "__main__":
    set_day()
    print [item for row in timer for item in row]
