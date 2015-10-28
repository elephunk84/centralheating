#/bin/python
from datetime import date, datetime, timedelta
from dateutil import parser
run_time=[1, "14:00", "16:30"]
ch_on=datetime.strptime((run_time[1]), '%H:%M')
ch_off=datetime.strptime((run_time[2]), '%H:%M')

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

for results in perdelta(datetime.time(ch_on), datetime.time(ch_off), timedelta(minutes=1)):
    print results 
