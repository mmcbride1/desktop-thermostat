#!/usr/bin/python

import time
import explorerhat as hat

# Class: LEDAssembly #
'''
Encapsulates functionality 
of three-part LED assembly
that indicates ambient 
temperature levels
'''

class LEDAssembly:

   ''' 
   Set the assembly state
   '''
   def set_range_led(self, led, mod):

      self.led = led
      self.mod = mod

      if mod == 'on':
         return {

          'low' : hat.output.one.on,
          'mid' : hat.output.two.on,
          'crt' : hat.output.three.on,

         }[led]()

      elif mod == 'off':
         return {

          'low' : hat.output.one.off,
          'mid' : hat.output.two.off,
          'crt' : hat.output.three.off,

         }[led]()

      else:
         print "Bad Output Directive!"

   ''' 
   Display a warn pattern
   '''
   def warn_signal(self, led):

      self.led = led
      self.set_range_led(led, 'on')
      time.sleep(0.25)
      self.set_range_led(led, 'off')
      time.sleep(0.25)

   '''
   Cleanup LED member status
   '''
   def cleanup(self):
   
      self.set_range_led('low', 'off')
      self.set_range_led('mid', 'off')
      self.set_range_led('crt', 'off')
      sys.exit()
