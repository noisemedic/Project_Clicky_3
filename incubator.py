# THE GEIGER COUNTER IT GO BEEEEEEEEEEEEEEEP

import time
import datetime
import RPi.GPIO as GPIO
from collections import deque

GPIO.setmode(GPIO.BOARD)

geigerIn = 8
buzzerOut = 10
GPIO.setup(gmIN,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(buzzerOut,GPIO.OUT)

counts = 0
counts_5sec = 0
beep = 0


#first create a perpetual timer class
#example from http://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

#now define our own function to count down the timer
def countmeThread():
  global beep
  if beep == 0:
    GPIO.output(buzzerOut,0)
    print("NO BUZZ FOR YOU")
  else:
    beep = beep - 1
    print("BUZZY BUZZ BUZZ! Total counts: ",counts_now)
    GPIO.output(buzzerOut,1) # on
    time.sleep(1.5) # wait 0.15 seconds
    GPIO.output(buzzerOut,0) # off
    time.sleep(3.5) # wait 0.35 seconds

#Let's start the Timer Thread
t = perpetualTimer(0.1,countmeThread)
t.start()

# when the detection event procs, it will call the function countme

def countme(channel):
    global counts
    beep = 50 # timer is set in 0.1 sec increments, 50 = 5 seconds
    GPIO.output(buzzerOut,1) # buzz immediately

# detection event proc'd from a falling edge event
GPIO.add_event_detect(geigerIn,GPIO.FALLING,callback=countme)

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

"""
GPIO.setup(8,GPIO.IN)
GPIO.add_event_detect(8,GPIO.FALLING)
GPIO.add_event_callback(8,countme)

"""
# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(8, GPIO.IN)
# ?remove callback feature
GPIO.add_event_detect(8, GPIO.BOTH, callback=countme)
#GPIO.add_event_detect(8, GPIO.FALLING)
#GPIO.add_event_callback(8, countme)

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
