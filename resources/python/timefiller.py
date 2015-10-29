#/bin/python
from datetime import date, datetime, timedelta
from dateutil import parser
import schedule

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta



