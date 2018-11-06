#!/usr/bin/python3

# ECE434
# Russell Johnson & Griffin Steffy

import time
import datetime
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment

# init pin for button/switch
GPIO.setup("P9_26", GPIO.IN)

# setup variables to control 7 segment displays
segment1 = SevenSegment.SevenSegment(address=0x70)
segment2 = SevenSegment.SevenSegment(address=0x71)

# init 7 segment displays
segment1.begin()
segment2.begin()

# variables to track players scores
home_score = 0
away_score = 0

# variable to track current player: 1 = home, 0 = away
current = 1
last = 0

# zeros to fill in for scores on displays
zeros = {
    0 : "0000",
    1 : "000",
    2 : "00",
    3 : "0",
    4 : ""
}

# 7 segment control examples
#segment.set_digit(0, 1) # set tens digits of left side of display to 1
#segment.set_digit(1, 1) # set ones digits of left side of display to 1
#segment.set_digit(2, 1) # set tens digits of right side of display to 1
#segment.set_digit(3, 1) # set ones digits of right side of display to 1
#segment.set_colon(freq) # set colon at freq

def ir_broken(channel):
    global last, current, home_score, away_score, segment1, segment2
    if last != current :
        last = current

        # Home
        if current == 1:
            print "Home Team Scored"

            # Update score and convert to a string
            home_score += 10
            score_str = str(home_score)
            score_str = zeros[len(score_str)] + score_str

            # display score to Home's display
            segment2.clear()
            segment2.set_digit(0, int(score_str[0]))
            segment2.set_digit(1, int(score_str[1]))
            segment2.set_digit(2, int(score_str[2]))
            segment2.set_digit(3, int(score_str[3])) 
            segment2.write_display()

        # Away
        else:
            print "Away Team Scored"

            # Update score and convert to a string
            away_score += 10
            score_str = str(away_score)
            score_str = zeros[len(score_str)] + score_str

            # display score to Away's display
            segment1.clear()
            segment1.set_digit(0, int(score_str[0]))
            segment1.set_digit(1, int(score_str[1]))
            segment1.set_digit(2, int(score_str[2]))
            segment1.set_digit(3, int(score_str[3]))
            segment1.write_display()

def btn_press(channel):
    global last, current
    last = current

    if GPIO.input("P9_26"):
    	GPIO.output("P9_41", GPIO.HIGH)
	GPIO.output("P9_42", GPIO.LOW)
        current = 0
    	print "Away Team's Turn"
    else:
	GPIO.output("P9_42", GPIO.HIGH)
        GPIO.output("P9_41", GPIO.LOW)
	current = 1
	print "Home Team's Turn"
    
def reset():
    global segment1, segment2, current, last, home_score, away_score

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

    # reset scoring variables
    btn_press(1)

    home_score = 0
    away_score = 0

def main():   
    # init pins for ir sensors
    GPIO.setup("P9_11", GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup("P9_13", GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup("P9_14", GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup("P9_15", GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup("P9_16", GPIO.IN, pull_up_down=GPIO.PUD_UP) 

    # init pins for buttons
    GPIO.setup("P9_26", GPIO.IN) 
    GPIO.setup("P9_27", GPIO.IN)   

    GPIO.setup("P9_41", GPIO.OUT, pull_up_down=GPIO.PUD_UP)
    GPIO.setup("P9_42", GPIO.OUT, pull_up_down=GPIO.PUD_UP)

    print "Press CTRL+Z to exit"
    print ""
    reset()

    # setup interrupts for IR sensors
    GPIO.add_event_detect("P9_11", GPIO.FALLING, callback=ir_broken)
    GPIO.add_event_detect("P9_13", GPIO.FALLING, callback=ir_broken)
    GPIO.add_event_detect("P9_14", GPIO.FALLING, callback=ir_broken)
    GPIO.add_event_detect("P9_15", GPIO.FALLING, callback=ir_broken)
    GPIO.add_event_detect("P9_16", GPIO.FALLING, callback=ir_broken)

    # setup interrupts for buttons
    GPIO.add_event_detect("P9_26", GPIO.BOTH, callback=btn_press, bouncetime=200)
    GPIO.add_event_detect("P9_27", GPIO.RISING, callback=reset, bouncetime=200)     
    
    while(True):
        empty = 1
main()
