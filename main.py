# THE GEIGER COUNTER IT GO BEEEEEEEEEEEEEEEP

import time
import datetime
import RPi.GPIO as GPIO
from collections import deque

GPIO.setmode(GPIO.BOARD)
counts = deque()
counts_5sec = 0

# This method fires on edge detection (the pulse from the counter board)
def countme(channel):
    global counts, hundredcount
    timestamp = datetime.datetime.now()
    counts.append(timestamp)

# This pulses the buzzer
def clickity():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.85)

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

    try:
        while counts[0] < datetime.datetime.now() - datetime.timedelta(seconds=60):
            counts.popleft()
    except IndexError:
        pass # there are no records in the queue.

    if loop_count == 10:
        # Every 10th iteration (10 seconds), store a measurement in Influx
        counts_now = int(len(counts))
        if counts_now > counts_5sec:
            print("The geiger counter it go BEEP")
            clickity()
        else:
            print("The geiger counter it not go BEEP")

        loop_count = 0
    time.sleep(1)
