#!/usr/bin/python
import json
import datetime
import sys
from pprint import pprint
import os
now = datetime.datetime.now()
global timer
timer=""
Monday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Tuesday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Wednesday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Thursday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Friday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Saturday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  
Sunday = [
          [1, ["04:00"], ["05:15"]],
          [2, ["04:00"], ["05:15"]],
          [3, ["04:00"], ["05:15"]],
          [4, ["04:00"], ["05:15"]],
          [5, ["04:00"], ["05:15"]],
          [6, ["04:00"], ["05:15"]],
          [7, ["04:00"], ["05:15"]],
          [8, ["04:00"], ["05:15"]],
          [9, ["04:00"], ["05:15"]],
          [0, ["04:00"], ["05:15"]],

          ]  

def print_day():
    today=now.strftime("%A")
    if today == "Monday":
        timer=Monday
        print today
        print timer
    elif today == "Tuesday":
        timer=Tuesday
        print today
        print timer
    elif today == "Wednesday":
        timer=Wednesday
        print today
        print timer
    elif today == "Thursday":
        timer=Thurssday
        print today
        print timer
    elif today == "Friday":
        timer=Friday
        print today
        print timer
    elif today == "Saturday":
        timer=Saturday
        print today
        print timer
    elif today == "Sunday":
        timer=Sunday
        print today
        print timer
    else:
        dumpclean(Week)

if __name__ == "__main__":
    print_day()
