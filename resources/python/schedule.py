#!/usr/bin/python
import json
import datetime
import sys
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
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

          ]  
Tuesday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

          ]  
Wednesday = [
<<<<<<< HEAD
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
=======
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]
>>>>>>> 3e73b4ed3a33ad07ab4162ae9984fc3cb01256fb

          ]  
Thursday = [

          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

          ]  
Friday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

          ]  
Saturday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

          ]  
Sunday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["07:00"], ["08:15"]],
          [3, ["00:00"], ["00:15"]],
          [4, ["00:00"], ["00:15"]],
          [5, ["10:00"], ["11:00"]],
          [6, ["00:00"], ["00:00"]],
          [7, ["14:00"], ["15:15"]],
          [8, ["17:00"], ["20:00"]],
          [9, ["22:00"], ["11:30"]],
          [0, ["00:00"], ["00:00"]]

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
    on_times=[i[1] for i in timer]
    off=[i[2] for i in timer]
    if timenow in on_times:
        __builtin__.status="ON"
        print "Schedule: ON"
    elif timenow in off:
        __builtin__.status="OFF"
        print "Schedule: OFF"
    else:
        print "No Status Change"

def print_timer():
    for n in timer:
        print n
    print timer[3]
    
        

if __name__ == "__main__":
    set_day()
