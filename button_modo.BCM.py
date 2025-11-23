# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 01:39:36 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time 

def modo_BCM ():
    GPIO.setwarnings (False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(25, GPIO.IN)

    while True:
        if GPIO.input(25):
            GPIO.output(18, False)
        else:
            GPIO.output(18, True)
modo_BCM()