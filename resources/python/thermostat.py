#!/usr/bin/env python
#
# A very simple dumb thermostat.
#

from time import sleep


class SimpleThermostat(object):
    """A SimpleThermostat is the simplest form of temperature controller.
    Given a sensor, actuator and target temperature is will turn on
    the heating when the temperature is bellow the target, otherwise
    it will turn it off."""

    def __init__(self, sensor, actuator, target=21, period=30):
        self.sensor = sensor
        self.actuator = actuator
        self.target = target
        self.period = period

    def run(self):
        """
        Run the thermostat until interrupted
        """
        while True:
            self.sensor.poll()
            temp = self.sensor.last_value()
            if temp < self.target:
                print "Turning on"
                self.actuator.set(True)
            else:
                print "Turning off"
                self.actuator.set(True)

            sleep(self.period)
                
                
