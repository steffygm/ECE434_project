#!/usr/bin/python

import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment1 = SevenSegment.SevenSegment(address=0x70)
segment2 = SevenSegment.SevenSegment(address=0x71)

# Initialize the displays. Must be called once before using the displays.
segment1.begin()
segment2.begin()

print "Press CTRL+Z to exit"

# Continually update the time on a 4 char, 7-segment display
while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  segment1.clear()
  segment2.clear()
  
  # Set hours
  segment1.set_digit(0, int(hour / 10))     # Tens
  segment1.set_digit(1, hour % 10)          # Ones
  segment2.set_digit(0, int(hour / 10))     # Tens
  segment2.set_digit(1, hour % 10)          # Ones
  
  # Set minutes
  segment1.set_digit(2, int(minute / 10))   # Tens
  segment1.set_digit(3, minute % 10)        # Ones
  segment2.set_digit(2, int(minute / 10))   # Tens
  segment2.set_digit(3, minute % 10)        # Ones

  # Toggle colon
  segment1.set_colon(second % 2)              # Toggle colon at 1Hz
  segment2.set_colon(second % 2)              # Toggle colon at 1Hz

  # Write the display buffer to the hardware.  This must be called to
  # update the actual display LEDs.
  segment1.write_display()
  segment2.write_display()

  # Wait a quarter second (less than 1 second to prevent colon blinking getting$
  time.sleep(0.25)
