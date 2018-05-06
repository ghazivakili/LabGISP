#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED = 25
GPIO.setup(LED,GPIO.OUT)
def blink(pin):
GPIO.output(pin, True)
    time.sleep(0.5)
    GPIO.output(pin, False)
    time.sleep(0.5)
for i in range (0,50):
    blink(LED)   # GPIO pin 25
GPIO.cleanup()
