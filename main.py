# THE GEIGER COUNTER IT GO BEEEEEEEEEEEEEEEP

import time
import datetime
import RPi.GPIO as GPIO
from collections import deque

GPIO.setmode(GPIO.BOARD)
counts = 0
counts_5sec = 0

# This method fires on edge detection (the pulse from the counter board)
def countme(channel):
    global counts
    counts = counts + 1

# This pulses the buzzer
def clickity():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.35)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.35)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.35)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.35)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.35)

# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(8, GPIO.IN)
# ?remove callback feature
# GPIO.add_event_detect(8, GPIO.FALLING, callback=countme)
GPIO.add_event_detect(8, GPIO.FALLING, callback=countme)

# Set the output pin
GPIO.setup(10, GPIO.OUT)

loop_count = 0

# In order to calculate CPM we need to store a rolling count of events in the last 60 seconds
# This loop runs every second to update the Nixie display and removes elements from the queue
# that are older than 60 seconds
while True:
    loop_count = loop_count + 1

    if loop_count == 10:
        # Every 10th iteration (10 seconds), store a measurement in Influx
        counts_now = counts

        if counts_now > counts_5sec:
            print("The geiger counter it go BEEP")

        else:
            print("The geiger counter it not go BEEP")
            clickity()
        counts_5sec = counts_now

        loop_count = 0
    time.sleep(1)
GPIO.cleanup()
