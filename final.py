import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math
import urllib
import sys
import signal
import csv

#pwm duty
#PWM.start("P9_ ,50)
GPIO.setup("P9_22",GPIO.OUT)
GPIO.setup("P9_24",GPIO.OUT)
#GPIO.setup("P9_16",GPIO.OUT)

while True:

          try:
	    #prev = 	    
            
            #cmd = inturllib.urlopen("https://api.thingspeak.com/channels/126928/fields/1/last.txt").read())
            valuefile = open('state.csv')
            reader = csv.reader(valuefile)
            values = list(reader)
            #myList = list(values[0])
	   
		
            pwm = int(values[0][1])
            bulb = int(values[0][0])
#	    print "cmd=%s\nfan=%s" %(cmd, fan)
            #print(
            if pwm == 1:
                        #print "1-ON"
                  GPIO.output("P9_24", GPIO.HIGH)
            else :
 #                 print "I am here"
                  GPIO.output("P9_24", GPIO.LOW)
            

           # a = int(urllib.urlopen("https://api.thingspeak.com/channels/126928/fields/2/last.txt").read())
            #            if a == 1:
                        
            

            #fan = int(urllib.urlopen("https://api.thingspeak.com/channels/126928/fields/3/last.txt").read())
            if bulb != 0 :
                   #print "1-ON"
                  GPIO.output("P9_22", GPIO.HIGH)
                        
            else :
                  #print "1- OFF"
                  GPIO.output("P9_22", GPIO.LOW)
          
          except KeyboardInterrupt:
                     print "CLEAN UP"
                     GPIO.cleanup()
                     sys.exit(0)

          time.sleep(1)

