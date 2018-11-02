#!/usr/bin/python3

import time
import datetime
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment

# init pins for ir sensors
GPIO.setup("P9_11", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_13", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_14", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_15", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_16", GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setup variables to control 7 segment displays
segment1 = SevenSegment.SevenSegment(address=0x70)
segment2 = SevenSegment.SevenSegment(address=0x71)

# init 7 segment displays
segment1.begin()
segment2.begin()

# setup variables for detecting if an ir beam has been broken
broken1 = 0
broken2 = 0
broken3 = 0
broken4 = 0
broken5 = 0

print "Press CTRL+Z to exit"

while (True):
    segment1.clear()
    segment2.clear()
    
    # Set hours
    #segment1.set_digit(0, int(hour / 10))     # Tens
    #segment1.set_digit(1, hour % 10)          # Ones
    #segment2.set_digit(0, int(hour / 10))     # Tens
    #segment2.set_digit(1, hour % 10)          # Ones
    
    # Set minutes
    segment1.set_digit(2, 1)   # Tens
    segment1.set_digit(3, 0)        # Ones
    segment2.set_digit(2, 1)   # Tens
    segment2.set_digit(3, 0)        # Ones

    # Toggle colon
    #segment1.set_colon(second % 2)              # Toggle colon at 1Hz
    #segment2.set_colon(second % 2)              # Toggle colon at 1Hz

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment1.write_display()
    segment2.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    #time.sleep(0.25)

    # ir sensors
    if not GPIO.input("P9_11"):
            if not broken1:
                    broken1 = 1
                    print("Broken1")
    else:
            broken1 = 0
    
    if not GPIO.input("P9_15"):
            if not broken2:
                    broken2 = 1
                    print("Broken2")
    else:
            broken2 = 0

    if not GPIO.input("P9_13"):
            if not broken3:
                    broken3 = 1
                    print("Broken3")
    else:
            broken3 = 0
    
    if not GPIO.input("P9_14"):
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