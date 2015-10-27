#!/usr/bin/python
import json
import datetime
import sys
import os
now = datetime.datetime.now()
Monday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Tuesday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
           } 
Wednesday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Thursday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Friday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Saturday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Sunday = {
                '1': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '2': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '3': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '4': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '5': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '6': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '7': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '8': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}},
                '9': {'On': {'hour': '07', 'minute': '00'}, 'Off': {'hour': '07', 'minute': '45'}}
          } 
Week = {
                'Monday' : json.dumps(Monday),
                'Tuesday' : json.dumps(Tuesday),
                'Wednesday' : json.dumps(Wednesday),
                'Thursday' : json.dumps(Thursday),
                'Friday' : json.dumps(Friday),
                'Saturday' : json.dumps(Saturday),
                'Sunday' : json.dumps(Sunday)

       }

def dumpclean(obj):
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print u'{0}: {1}'.format(k, v)

    else:
        print obj

def print_day():
    today=now.strftime("%A")
    dump=today
    print dump
    if dump == "Monday":
        global timer
        timer = dumpclean(Monday)
        return timer
    elif dump == "Tuesday":
        dumpclean(Tuesday)
    elif dump == "Wednesday":
        dumpclean(Wednesday)
    elif dump == "Thursday":
        dumpclean(Thursday)
    elif dump == "Friday":
        dumpclean(Friday)
    elif dump == "Saturday":
        dumpclean(Saturday)
    elif dump == "Sunday":
        dumpclean(Sunday)
    else:
        dumpclean(Week)

