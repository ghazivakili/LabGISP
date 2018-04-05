#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED = 25
BUTTON = 23
state = False
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN, GPIO.PUD_UP)
while True:
    if GPIO.input(BUTTON) == False:  # Button pressed
        state = True
    else:
        state = False
    GPIO.output(LED,state)  # time.sleep(0.1) to test every 0.1s
GPIO.cleanup()
