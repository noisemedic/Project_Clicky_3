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
    counts += 1

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

# This pulses the buzzer
def clickity2():
    GPIO.output(10, GPIO.HIGH) # shave
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.40)
    GPIO.output(10, GPIO.HIGH) # and
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(10, GPIO.HIGH) # a
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(10, GPIO.HIGH) # hair
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.40)
    GPIO.output(10, GPIO.HIGH) # cur
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)
    GPIO.output(10, GPIO.HIGH) # two
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(10, GPIO.HIGH) #bits
    time.sleep(0.10)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)


# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(8, GPIO.IN)
# ?remove callback feature
# GPIO.add_event_detect(8, GPIO.FALLING, callback=countme)
GPIO.add_event_detect(8, GPIO.FALLING)
GPIO.add_event_callback(8, self.countme)

# Set the output pin
GPIO.setup(10, GPIO.OUT)

loop_count = 0

# In order to calculate CPM we need to store a rolling count of events in the last 60 seconds
# This loop runs every second to update the Nixie display and removes elements from the queue
# that are older than 60 seconds
while True:
    loop_count = loop_count + 1

    if loop_count == 5:
        # Every 5h iteration (5 seconds), compare it to 5 seconds ago, if higher then BEEP
        counts_now = counts
        print("Total counts:", counts_now)
        if counts_now > counts_5sec:
            print("The geiger counter it go BEEP")

        else:
            print("The geiger counter it not go BEEP")
            clickity2()
        counts_5sec = counts_now

        loop_count = 0
    time.sleep(1)

GPIO.cleanup()
