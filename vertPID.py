import os
import serial
import time
os.system("sudo pigpiod")
time.sleep(1)
import pigpio
import sys
import program

ESC1=13
ESC2=12
ESC3=18
ESC4=19

max_value = 1500
min_value = 970
pi=pigpio.pi();

