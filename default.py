#!/bin/python

import os
import sys
import time
import datetime
import pytz
from tzlocal import get_localzone

from dateutil.tz import tzlocal


def localTzname():
    if time.daylight:
        offsetHour = time.altzone / 3600
        print offsetHour
    else:
        offsetHour = time.timezone / 3600
        print offsetHour
    return 'Etc/GMT%+d' % offsetHour


if __name__ == "__main__":
    localtime = time.ctime()
    print "Local current time :", localtime
