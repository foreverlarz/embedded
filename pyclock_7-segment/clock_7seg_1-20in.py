#!/usr/bin/python

import time
import datetime
from Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

print "Press CTRL+Z to exit."

digit2_colon = 0x02
digit2_dot = 0x10
digit0 = 0

while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  dots = 0x0
  dots = dots^digit2_dot if (hour >= 12) else dots
  dots = dots^digit2_colon if (second % 2) else dots
  if hour == 0:
    hour = 12
  if hour > 12:
    hour = hour - 12
  if (hour >= 10 and digit0 == 0):
    segment.writeDigit(0, 1)
    digit0 = 1
  if (hour < 10 and digit0 == 1):
    segment.disp.clear()
    digit0 = 0
  segment.writeDigit(1, hour % 10)
  segment.writeDigitRaw(2, dots)
  segment.writeDigit(3, int(minute / 10))
  segment.writeDigit(4, minute % 10)
  time.sleep(0.25)

