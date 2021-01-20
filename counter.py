# THE GEIGER COUNTER IT GO BEEEEEEEEEEEEEEP

import time
import datetime
import RPi.GPIO as GPIO
from collections import deque
# from influxdb import InfluxDBClient

GPIO.setmode(GPIO.BOARD)

counts = deque()
hundredcount = 0
counts_5sec = 0
#usvh_ratio = 0.00812037037037 # This is for the J305 tube
usvh_ratio = 0.00277 # This is for the SBM20 tube

# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(8, GPIO.IN)
# ?remove callback feature
# GPIO.add_event_detect(8, GPIO.FALLING, callback=countme)
GPIO.add_event_detect(8, GPIO.FALLING)

# Set the output pin
GPIO.setup(10, GPIO.OUT)

loop_count = 0

# In order to calculate CPM we need to store a rolling count of events in the last 60 seconds
# This loop runs every second to update the Nixie display and removes elements from the queue
# that are older than 60 seconds
while True:
    loop_count = loop_count + 1

    try:
        while counts[0] < datetime.datetime.now() - datetime.timedelta(seconds=60):
            counts.popleft()
    except IndexError:
        pass # there are no records in the queue.

    if loop_count == 10:
        # Every 10th iteration check if counts_now>counts_5sec
        counts_now = int(len(counts))
        if counts_now > counts_5sec:
            print("Current counts:",counts_now)
            GPIO.output(10, GPIO.HIGH)
            time.sleep(0.15)
            GPIO.output(10, GPIO.LOW)
            time.sleep(0.85)
            GPIO.output(10, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(10, GPIO.LOW)
            time.sleep(0.75)
            GPIO.output(10, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(10, GPIO.LOW)
            time.sleep(0.75)
            counts_5sec = counts_now

        loop_count = 0

time.sleep(1)
