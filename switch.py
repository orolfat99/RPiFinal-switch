#!/usr/bin/python3
 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
while True:
        switch = GPIO.input(17)
        if switch == 1:
                print("***switch on***")
        else:
                print("***switch off***")
        time.sleep(1)
GPIO.cleanup()
