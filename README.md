# BBB-Home-Automation
This project was built when I was interning in Texas Instrument's CEPD Summer Internship 2016 in NSIT.
This project focuses on building an IoT solution to control the electric appliances of a house via a mobile phone app. In this project we had built a prototype wherein the Lights and fans were controlled via the app.

Hardware Requirements:-
  MicroController - Beagle Bone Black
  Self Fabricated Cape :- Ref,Value ,Note
                           C1,0.01uF,C-EU075-032X103
                           C8,0.01uF,C-EU075-032X104
                           D1,1N4007,DO41-10
                           OK1,4N35,MOTOROLA OPTO COUPLER
                           OK2,MOC3041,6-Pin DIP Zero-Cross Optoisolators Triac Driver 
                           OK4,MOC3021M,RANDOM-PHASE OPTOISOLATORS TRIAC DRIVER 
                            R1,1M,1/8WATT
                            R2,1K,1/8WATT
                            R5,330,1/8WATT
                            R6,360,1/8WATT
                            R7,330,1/8WATT
                            R8,39,1/8WATT
                            R9,330,1/8WATT
                            R10,360,1/8WATT
                            R12,39,1/8WATT
                            R13,330,1/8WATT
                            T1,BT148,THYRISTOR
                            T3,BT148,THYRISTOR
                            X2,,PTR Connector
                            X3,,PTR Connector
                            X4,,PTR Connector

A cape for Beagle Bone Black was fabricated to help isolate the low voltage DC circuit of BBB from the high voltage AC circuit of home appliances. With the help of the cape, simple digitar signals from the IO pins for BBB could turn on/off the lights and the output from pwm coud control the fan speed.

We devised two ways for the mobile app and BBB to communicate.
      1)Local Web Server
      2)Cloud (thinkspeak)
Whenever the mobile phone and the BBB were connected to the same network, all communications would occur via the local network itself. The advantage was that all communications were fast and in real time.
But when they were connected in different networks, the communication would take place through the could channel.Thus a person can control his home appliances from any part of the globe.

The prototype was succesfully developed and designed at NSIT.
