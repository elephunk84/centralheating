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
    global now
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
    global ch_off
    global ch_off
    global ch_status
    sublistcheck=''
    timenow=now.strftime("%H:%M")
    time_now=timenow
    nexthour=datetime.datetime.now() + datetime.timedelta(minutes=60)
    print "Time now is.....\n" +  today, timenow
    for sublist in timer:
        if (sublist[1] <= timenow) and (sublist[2] >= timenow):
            chon=sublist[1]
            choff=sublist[2]
            print "--------------------------------------"
            print "Active Program...."
            print "On: "+ chon, "Off: "+ choff
            print "--------------------------------------"
            ch_on = datetime.datetime.strptime(chon, '%H:%M')
            ch_off = datetime.datetime.strptime(choff, '%H:%M')
            f = open('resources/run_schedule','w')
            f.write(chon + '\n' + choff)
            f.close()
            ch_status="ON"
        else:
            print "Program Not Active...."
            f = open('resources/run_schedule','w')
            f.write('')
            f.close()
    for sublist in timer: 
        if (sublist[1] >= timenow):
            if sublist[1] <= str(nexthour):
                program=("On: " + sublist[1] + "  Off: " + sublist[2])
                print "--------------------------------------"
                print "Next Active Program...."
                print program
                f = open('resources/next_run','w')
                f.write("On: " + sublist[1] +  " Off: " + sublist[2])
                f.close()
            else:
                pass
        else:
            pass

if __name__ == "__main__":
    set_day()
