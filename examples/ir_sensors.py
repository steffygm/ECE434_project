#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_26", GPIO.IN, pull_up_down=GPIO.PUD_UP)

broken = 0

while 1:
        if not GPIO.input("P9_26"):
                if not broken:
                        broken = 1
                        print("Broken")
        else:
                broken = 0

