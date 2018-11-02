#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_11", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_13", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_14", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_15", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_16", GPIO.IN, pull_up_down=GPIO.PUD_UP)

broken1 = 0
broken2 = 0
broken3 = 0
broken4 = 0
broken5 = 0

while 1:
        if not GPIO.input("P9_11"):
                if not broken1:
                        broken1 = 1
                        print("Broken1")
        else:
                broken1 = 0
        
        if not GPIO.input("P9_13"):
                if not broken2:
                        broken2 = 1
                        print("Broken2")
        else:
                broken2 = 0

        if not GPIO.input("P9_14"):
                if not broken3:
                        broken3 = 1
                        print("Broken3")
        else:
                broken3 = 0
        
        if not GPIO.input("P9_15"):
                if not broken4:
                        broken4 = 1
                        print("Broken4")
        else:
                broken4 = 0

        if not GPIO.input("P9_16"):
                if not broken5:
                        broken5 = 1
                        print("Broken5")
        else:
                broken5 = 0