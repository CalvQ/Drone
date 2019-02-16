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
pi.set_servo_pulsewidth(ESC1, max_value)
pi.set_servo_pulsewidth(ESC2, max_value)
pi.set_servo_pulsewidth(ESC3, max_value)
pi.set_servo_pulsewidth(ESC4, max_value)
  #print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
time.sleep(5)
print "Hang in there..."
pi.set_servo_pulsewidth(ESC1, min_value)
pi.set_servo_pulsewidth(ESC2, min_value)
pi.set_servo_pulsewidth(ESC3, min_value)
pi.set_servo_pulsewidth(ESC4, min_value)
time.sleep(5)
print "Keep Hanging..."
pi.set_servo_pulsewidth(ESC1, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.set_servo_pulsewidth(ESC3, 0)
pi.set_servo_pulsewidth(ESC4, 0)
time.sleep(5)
print "Almost there"
pi.set_servo_pulsewidth(ESC1, min_value)
pi.set_servo_pulsewidth(ESC2, min_value)
pi.set_servo_pulsewidth(ESC3, min_value)
pi.set_servo_pulsewidth(ESC4, min_value)
time.sleep(5)

#ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
norm = 1040
pi.set_servo_pulsewidth(ESC1, norm)
pi.set_servo_pulsewidth(ESC2, norm)
pi.set_servo_pulsewidth(ESC3, norm)
pi.set_servo_pulsewidth(ESC4, norm)
#//////////////////////////////////////////////////////////////////////////////////

#Setup Variables
rad_to_deg = 180/3.141592654
