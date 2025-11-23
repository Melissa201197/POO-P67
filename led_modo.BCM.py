# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 01:35:58 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time

def modo_BCM():

    GPIO.setwarnings (False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    while True:
        GPIO.output(18, True)
        time.sleep(1)
        GPIO.output(18, False)
        time.sleep(1)
modo_BCM()