import RPi.GPIO as GPIO
from threading import Timer,Thread,Event
import time

#set BCM MODE

GPIO.setmode(GPIO.BOARD)

geigerIn = 8
buzzerOut = 10
GPIO.setup(geigerIn,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(buzzerOut,GPIO.OUT)

counts = 0
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
    print("NO BUZZ FOR YOU! Total counts: ",counts)
  else:
    beep = beep - 1
    print("BUZZY BUZZ BUZZ! Total counts: ",counts)
    GPIO.output(buzzerOut,1) # on
    time.sleep(1.5) # wait 0.15 seconds
    GPIO.output(buzzerOut,0) # off
    time.sleep(3.5) # wait 0.35 seconds

#Let's start the Timer Thread
t = perpetualTimer(0.1,countmeThread)
t.start()

# when the detection event procs, it will call the function countme

def countme(channel):
    global beep
    global counts
    counts += 1
    beep = 50 # timer is set in 0.1 sec increments, 50 = 5 seconds
    GPIO.output(buzzerOut,1) # buzz immediately

# detection event proc'd from a falling edge event
GPIO.add_event_detect(geigerIn,GPIO.FALLING,callback=countme)
try :

   while True:
    # do your loop for others things here
    time.sleep(0.01)   #this is added to decrease cpu usage since there is nothing in the loop


except KeyboardInterrupt:
   quit()
