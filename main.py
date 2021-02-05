# THE GEIGER COUNTER IT GO BEEEEEEEEEEEEEEEP
import time
#import datetime
from threading import Timer,Thread,Event
import RPi.GPIO as GPIO
from collections import deque

#GPIO.setmode(GPIO.BOARD)
#counts = 0
counts_5sec = 0

class Geigercounter (threading.Thread):
    def __init__(self,counts=0):
        log.info("Unleash the clicks!")
        threading.Thread.__init__(self)
        self.daemon = True
        self.socket = None

        self.reset()
        self.start()

    def reset(self):
        self.count=0

    def tick(self, pin=none):
        self.count += 1

    def run(self):
        GPIO.setmode(GPIO.BCM)
        gpio_port = 8
        GPIO.setup(gpio_port, GPIO.IN)
        GPIO.add_event_detect(gpio_port,GPIO.FALLING)
        GPIO.add_event_callback(gpio_port,self.tick)

        counts_now = 0
        counts_5sec = self.count

        while True:
            time.sleep(1)

            counts_now = self.count

            if counts_now < counts_5sec:
                print("The geiger counter it not go BEEP")

            else:
                print("The geiger counter it go BEEEEEEEEEEEP")

            counts_5sec = counts_now
"""
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

GPIO.setup(8,GPIO.IN)
GPIO.add_event_detect(8,GPIO.FALLING)
GPIO.add_event_callback(8,countme)


# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(8, GPIO.IN)
# ?remove callback feature
GPIO.add_event_detect(8, GPIO.BOTH, callback=countme)
#GPIO.add_event_detect(8, GPIO.FALLING)
#GPIO.add_event_callback(8, countme)

# Set the output pin
GPIO.setup(10, GPIO.OUT)
"""
loop_count = 0

# In order to calculate CPM we need to store a rolling count of events in the last 60 seconds
# This loop runs every second to update the Nixie display and removes elements from the queue
# that are older than 60 seconds
while True:

    Geigercounter.start

    loop_count = loop_count + 1
"""
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
"""
GPIO.cleanup()
