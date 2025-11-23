# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 22:30:59 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time 

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    time.sleep(1)
    
    
    
    
    
    
    