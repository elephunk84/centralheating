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
global ch_on
global ch_off
global sublistcheckprint 
chon=""
choff=""
sublistcheck=''

Monday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "09:30", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

          ]  
Tuesday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

          ]  
Wednesday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

          ]  
Thursday = [

          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

          ]  
Friday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]

          ]  
Saturday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "17:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]
          ]
Sunday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "17:02", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]
          ]  

def set_day():
    global timer
    global today
    now = datetime.datetime.now()
    today=now.strftime("%A")
    if today == "Monday":
        timer=list(Monday)
        run_timer()
    elif today == "Tuesday":
        timer=list(Tuesday)
        run_timer()
    elif today == "Wednesday":
        timer=list(Wednesday)
        run_timer()
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
        pass

def run_timer():
    global timenow
    global time_now
    global today
    global ch_off
    global ch_off
    now = datetime.datetime.now()
    sublistcheck=''
    timenow=now.strftime("%H:%M")
    time_now=timenow
    now = datetime.datetime.now()
    today=now.strftime("%A")
    print "Time now is.....\n" +  today, timenow
    firstline = open("resources/run_schedule").readline().rstrip()
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
                f = open('resources/run_schedule','a')
                f.write(output+'\n' )
                f.close()
        elif sublist[2] == timenow:
            f = open('resources/run_schedule','w')
            f.write('')
            f.close()
            __builtin__.callback=''
        elif timenow in open('resources/run_schedule').read() and sublist[1] == firstline:
            chon=sublist[1]
            choff=sublist[2]
            print "--------------------------------------"
            print "Active Program...."
            print "On: "+ chon, "Off: "+ choff
            print "--------------------------------------"
        else:
            print "Program Not Active...."
    for sublist in timer: 
        if (sublist[1] >= timenow):
            nexthour=datetime.datetime.now() + datetime.timedelta(minutes=90)
            if sublist[1] <= str(nexthour):
                program=("On: " + sublist[1] + "  Off: " + sublist[2])
                print "--------------------------------------"
                print "Next Active Program...."
                print program
            else:
                pass
        else:
            pass

def print_timer():
    for n in timer:
        print n
    print timer[3]

if __name__ == "__main__":
    set_day()
