import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math
import urllib
import sys
import signal
import csv

#pwm duty
PWM.start("P9_14" ,0)
#GPIO.setup("P9_14",GPIO.OUT)
GPIO.setup("P9_15",GPIO.OUT)
GPIO.setup("P9_16",GPIO.OUT)

while True:

          try:
            
            cmd = inturllib.urlopen("https://api.thingspeak.com/channels/126928/fields/1/last.txt").read())
            #valuefile = open('state.csv')
            #reader = csv.reader(valuefile)
            #values = list(reader)
            #myList = list(values[0])
	   
		
            #cmd = int(values[0][0])
            #fan = int(values[0][1])
	    #print "cmd=%s\nfan=%s" %(cmd, fan)
            #print(
            if cmd != 0:
		  PWM.set_duty_cycle("P9_14", 25*cmd)
                        #print "1-ON"
                  #GPIO.output("P9_14", GPIO.HIGH)
            else :
                  print "I am here"
                  PWM.set_duty_cycle("P9_14", 0)
            

            #a = int(urllib.urlopen("https://api.thingspeak.com/channels/126928/fields/2/last.txt").read())
            #            if a == 1:
                        
            

            fan = int(urllib.urlopen("https://api.thingspeak.com/channels/126928/fields/3/last.txt").read())
            if fan != 0 :
                  print "fan -on"
                  GPIO.output("P9_15", GPIO.HIGH)
                        
            else :
                  print "fan off"
                  GPIO.output("P9_15", GPIO.LOW)
          
          except KeyboardInterrupt:
                     print "CLEAN UP"
                     GPIO.cleanup()
                     sys.exit(0)

          time.sleep(1)
