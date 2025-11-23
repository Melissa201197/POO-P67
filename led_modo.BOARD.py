# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 01:38:34 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time

def modo_BOARD():

    GPIO.setwarnings (False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)

    while True:
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(12, False)
        time.sleep(1)
modo_BOARD()