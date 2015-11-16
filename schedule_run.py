#!/bin/python
import os
import sys
import subprocess
lib_path = os.path.abspath(os.path.join('/home/pi/GitRepo/centralheating/', 'lib'))
sys.path.append(lib_path)

import __builtin__
import time
import datetime
import sqlite3
import glob
import socket
from resources.python import monitor
import resources.python.schedule_testing as schedule
from resources.python.schedule_testing import *
now=datetime.datetime.now()
today=now.strftime("%A")
time_now=time.strftime("%H:%M", time.localtime(time.time()))
logtime=time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
sublistcheck=''

if __name__ == "__main__":
    set_day()
