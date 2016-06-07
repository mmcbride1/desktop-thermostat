#!/usr/bin/python

from temperature_reading import TemperatureReading
from led_assembly import LEDAssembly
import ConfigParser
import time

# Class: Thermostat #
'''
Encapsulates the 
functionality of the 
thermostat recording
ambient temperature
'''

class Thermostat:

   # params #

   LOW = 0
   MID = 0
   CRT = 0

   '''
   Constructor
   '''
   def __init__(self):
      self.thermconfig()

   '''
   Threshold configuration
   '''
   def thermconfig(self):

      f = '/etc/thermostat.ini'
      cfg = ConfigParser.ConfigParser()
      cfg.read(f)

      self.LOW = int(cfg.get('settings','low'))
      self.MID = int(cfg.get('settings','mid'))
      self.CRT = int(cfg.get('settings','crt'))

      return
      
   '''
   Set indicator pattern
   '''
   def indicator(self, t):

      self.t = t

      # LED object #
      led = LEDAssembly()

      # Indicator logic #
      if t > self.LOW and t <= self.MID:
         led.set_range_led('crt', 'off')
         led.set_range_led('mid', 'off')
         led.set_range_led('low', 'on')
      elif t > self.MID and t <= self.CRT:
         led.set_range_led('crt', 'off')
         led.set_range_led('low', 'off')
         led.set_range_led('mid', 'on')
      else:
         led.set_range_led('low', 'off')
         led.set_range_led('mid', 'off')
         led.warn_signal('crt')

   '''
   Initiate and run the thermostat
   '''
   def engage_thermostat(self):
      
      # Loop temperature object #
      reading = TemperatureReading()
      while True:
         self.indicator(reading.gen_temperature_value())
