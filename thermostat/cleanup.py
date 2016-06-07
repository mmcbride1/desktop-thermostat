#!/usr/bin/python

from led_assembly import LEDAssembly

'''
Execute this script
upon service exit in
order to ensure all
LED members are shutdown
'''

# execute #

led = LEDAssembly()
led.cleanup()
