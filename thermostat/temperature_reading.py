#!/usr/bin/python

import explorerhat as hat

# Class: TemperatureReading #
''' 
Encapsulates voltage reading
from LM35 OSEPP temperature
sensor
'''

class TemperatureReading:

   # temperature value #
   TEMP = 0.0

   ''' 
   Constructor
   '''
   def __init__(self):
      self.set_temperature_value()

   ''' 
   Get analog reading
   '''
   def readmeter(self):
      return hat.analog.one.read()

   ''' 
   Generate temperature value
   '''
   def gen_temperature_value(self):
      volts = self.readmeter() * 100
      return ((volts * 9) / 5) + 32

   '''
   Set temperature value
   '''
   def set_temperature_value(self):
      self.TEMP = self.gen_temperature_value()

   ''' 
   Get temperature value
   '''
   def get_temperature_value(self):
      return self.TEMP
