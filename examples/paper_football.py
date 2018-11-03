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

# init pin for button/switch
GPIO.setup("P9_26", GPIO.IN)

# setup variables to control 7 segment displays
segment1 = SevenSegment.SevenSegment(address=0x70)
segment2 = SevenSegment.SevenSegment(address=0x71)

# init 7 segment displays
segment1.begin()
segment2.begin()

# variable to track button press
pressed = 0

# variables to track players scores
home_score = 0
away_score = 0

# variable to track current player: 1 = home, 0 = away
current = 1
last = 0

#segment.set_digit(0, 1) # set tens digits of left side of display to 1
#segment.set_digit(1, 1) # set ones digits of left side of display to 1
#segment.set_digit(2, 1) # set tens digits of right side of display to 1
#segment.set_digit(3, 1) # set ones digits of right side of display to 1
#segment.set_colon(freq) # set colon at freq

# clear displays
segment1.clear()
segment2.clear()

# set each score to 0000
segment1.set_digit(0, 0)        # Tens
segment1.set_digit(1, 0)        # Ones
segment1.set_digit(2, 0)        # Tens
segment1.set_digit(3, 0)        # Ones
segment2.set_digit(0, 0)        # Tens
segment2.set_digit(1, 0)        # Ones
segment2.set_digit(2, 0)        # Tens
segment2.set_digit(3, 0)        # Ones

# write to displays
segment1.write_display()
segment2.write_display() 

print "Press CTRL+Z to exit"

def ir_broken(channel):
    global last, current, home_score, away_score, segment1, segment2
    if last != current :
        last = current

        if current == 1:
            print "Home Team Scored"
            home_score += 10
            score_str = str(home_score)
            if len(score_str) < 3:
                score_str = "00" + score_str
            elif len(score_str) < 4:
                score_str = "0" + score_str

            segment2.clear()
            segment2.set_digit(0, int(score_str[0]))
            segment2.set_digit(1, int(score_str[1]))
            segment2.set_digit(2, int(score_str[2]))
            segment2.set_digit(3, int(score_str[3])) 
            segment2.write_display()

        else:
            print "Away Team Scored"
            away_score += 10
            score_str = str(away_score)
            if len(score_str) < 3:
                score_str = "00" + score_str
            elif len(score_str) < 4:
                score_str = "0" + score_str

            segment1.clear()
            segment1.set_digit(0, int(score_str[0]))
            segment1.set_digit(1, int(score_str[1]))
            segment1.set_digit(2, int(score_str[2]))
            segment1.set_digit(3, int(score_str[3]))
            segment1.write_display()

def btn_press(channel):
    global last, current
    last = current

    if current:
        current = 0
        print "Away Team's Turn"
    else:
        current = 1
        print "Home Team's Turn"
    
GPIO.add_event_detect("P9_11", GPIO.FALLING, callback=ir_broken)
GPIO.add_event_detect("P9_13", GPIO.FALLING, callback=ir_broken)
GPIO.add_event_detect("P9_14", GPIO.FALLING, callback=ir_broken)
GPIO.add_event_detect("P9_15", GPIO.FALLING, callback=ir_broken)
GPIO.add_event_detect("P9_16", GPIO.FALLING, callback=ir_broken)
GPIO.add_event_detect("P9_26", GPIO.RISING, callback=btn_press, bouncetime=200)


def main():        
    # empty
    print "Home Team's Turn"
    while(True):
        test = 1
main()