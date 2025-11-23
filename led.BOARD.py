# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 00:19:53 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time 

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
    GPIO.output(12, True)
    time.sleep(1)
    GPIO.output(12, False)
    time.sleep(1)
    
    