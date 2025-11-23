# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 01:41:22 2025

@author: NW
"""

import RPi.GPIO as GPIO
import time 

def modo_BOARD():
    GPIO.setwarnings (False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(22, GPIO.IN)

    while True:
        if GPIO.input(22):
            GPIO.output(12, False)
        else:
            GPIO.output(12, True)
modo_BOARD()