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
__builtin__.chstatus=''

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
          [5, "12:00", "14:30"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:59"],
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
          [9, "21:30", "23:00"],
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
          [7, "17:00", "20:30"],
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
    global nexthour
    sublistcheck=''
    timenow=now.strftime("%H:%M")
    time_now=str(timenow)
    next_hour=datetime.datetime.now() + datetime.timedelta(minutes=120)
    nexthour=next_hour.strftime("%H:%M")
    print "Time now is " +  today, timenow + "...."
    print "--------------------------------------"
    for sublist in timer:
        if (sublist[1] <= timenow) and (sublist[2] > timenow):
            chon=sublist[1]
            choff=sublist[2]
            print "--------------------------------------"
            print "Program "+ str(sublist[0]) +" Active...."
            print "On: "+ chon, "Off: "+ choff
            print "--------------------------------------"
            run_schedule=open('resources/run_schedule', 'w')
            run_schedule.write(chon + '\n' + choff)
            __builtin__.chstatus='ON'
        else:
            print "Program "+ str(sublist[0]) +" Not Active...."
    

def next_run():
    for sublist in timer: 
        if (sublist[1] >= timenow):
            if sublist[1] < str(nexthour):
                program=("On: " + sublist[1] + "  Off: " + sublist[2])
                print "Next Active Program...."
                print program
                print "--------------------------------------"
                f = open('resources/next_run','w')
                f.write("On: " + sublist[1] +  " Off: " + sublist[2])
                f.close()
            else:
                pass
        else:
            pass

def clean_up():
    for sublist in timer:
        if timenow in sublist[2]:
            with open('resources/run_schedule', 'w') as run, open('resources/status', 'w') as status:
                run.write('')
                status.write('')
                __builtin__.chstatus=''

if __name__ == "__main__":
    set_day()
    next_run()
    clean_up()
