#!/bin/python
import os
import sys
import datetime
import pprint
import copy
from schedule import *

now=datetime.datetime.now()
today=now.strftime("%A")
hour=now.strftime("%H")
minute=now.strftime("%M")
if today == "Monday":
    print Monday[1]
elif today == "Tuesday":
    Tuesday=today[0][1][0]
    strTuesday=Tuesday[:-3]
    print strTuesday
else:
    print "There was an error...."
