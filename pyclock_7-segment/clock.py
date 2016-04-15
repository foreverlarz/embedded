#!/usr/bin/python

import time
import datetime
from Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

print "Press CTRL+Z to exit."

while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  pm = 1 if (hour >= 12) else 0
  if hour == 0:
    hour = 12
  elif hour > 12:
    hour = hour - 12
  if hour >= 10:
    segment.writeDigit(0, 1)
  segment.writeDigit(1, hour % 10)
  segment.writeDigit(3, int(minute / 10))
  segment.writeDigit(4, minute % 10, pm)
  segment.setColon(second % 2)
  time.sleep(0.25)

