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
global timer
timer=""
global chon
global choff
chon=""
choff=""
global today
now = datetime.datetime.now()
today=now.strftime("%A")

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

          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:31", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

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

def run_timer():
    global timenow
    timenow=now.strftime("%H:%M")
    print "Time now is.....\n" +  today, timenow
    firstline = open("run_schedule").readline().rstrip()
    print firstline
    for sublist in timer:
        if sublist[1] == timenow:
            chon=sublist[1]
            choff=sublist[2]
            print "--------------------------------------"
            print "Active Program...."
            print "On: "+ chon, "Off: "+ choff
            print "--------------------------------------"
            ch_on = datetime.datetime.strptime(chon, '%H:%M')
            ch_off = datetime.datetime.strptime(choff, '%H:%M')
            for results in timefiller.perdelta((ch_on), (ch_off), datetime.timedelta(minutes=1)):
                out = str(results)
                output=out[11:-3]
                f = open('run_schedule','a')
                f.write(output+'\n' )
                f.close()
        elif timenow in open('run_schedule').read() and sublist[1] == firstline:
            chon=sublist[1]
            choff=sublist[2]
            print "--------------------------------------"
            print "Active Program...."
            print "On: "+ chon, "Off: "+ choff
            print "--------------------------------------"
        elif sublist[2] == timenow:
            f = open('run_schedule','w')
            f.write('')
            f.close()
        else:
            print "Program Not Active...."

def print_timer():
    for n in timer:
        print n
    print timer[3]

if __name__ == "__main__":
    set_day()
