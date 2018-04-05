#!/usr/bin/env python
import RPi.GPIO as GPIO
import time GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Broadcom SOC channel pin numbering
LED = 25
GPIO.setup(LED,GPIO.OUT)
print ("LED on")
GPIO.output(LED,GPIO.HIGH)  #True, or 1
time.sleep(5)
print ("LED off")
GPIO.output(LED,GPIO.LOW)  #False, or 0
GPIO.cleanup()
