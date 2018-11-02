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
any_broken = 0
broken1 = 0
broken2 = 0
broken3 = 0
broken4 = 0
broken5 = 0

# variables to track players scores
home_score = 0
away_score = 0

#segment.set_digit(0, 1) # set tens digits of left side of display to 1
#segment.set_digit(1, 1) # set ones digits of left side of display to 1
#segment.set_digit(2, 1) # set tens digits of right side of display to 1
#segment.set_digit(3, 1) # set ones digits of right side of display to 1
#segment.set_colon(freq) # set colon at freq

# clear displays
segment1.clear()
segment2.clear()

# set each score to 00
segment1.set_digit(2, 0)        # Tens
segment1.set_digit(3, 0)        # Ones
segment1.set_digit(2, 0)        # Tens
segment2.set_digit(3, 0)        # Ones

# write to displays
segment1.write_display()
segment2.write_display() 

print "Press CTRL+Z to exit"

while (True):
    if not GPIO.input("P9_11") or not GPIO.input("P9_15") or not GPIO.input("P9_13") or not GPIO.input("P9_14") or not GPIO.input("P9_16"):
        if not any_broken:
            any_broken = 1
            print("Borken")

            home_score += 6
            away_score += 6

            segment1.clear()
            segment2.clear()

            segment1.set_digit(2, int(home_score / 10))
            segment1.set_digit(3, home_score % 10)
            segment2.set_digit(2, int(away_score / 10))
            segment2.set_digit(3, away_score % 10) 

            segment1.write_display()
            segment2.write_display() 

    else:
        any_broken = 0