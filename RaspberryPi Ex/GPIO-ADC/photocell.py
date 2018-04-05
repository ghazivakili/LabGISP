#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PHOTOCELL = 24
def read(pin):
    reading = 0
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin,GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):  # 1ms per loop cycle
        reading += 1
    return reading
while True:
    print read(PHOTOCELL)
GPIO.cleanup()
