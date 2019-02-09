import os     #importing os library 
import serial
import time   #importing time 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #don't remove this, else you will get an error
import pigpio #importing GPIO library

ESC1=13  #ESC connections with the GPIO pins; note its the BROADCOM number, not the GPIO pin number!
ESC2=12
ESC3=18
ESC4=19
#max 1250, min 1020
max_value = 1500
min_value = 970
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, max_value)
pi.set_servo_pulsewidth(ESC2, max_value)
pi.set_servo_pulsewidth(ESC3, max_value)
pi.set_servo_pulsewidth(ESC4, max_value)
  #print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
                  
            pi.set_servo_pulsewidth(ESC1, min_value)
            pi.set_servo_pulsewidth(ESC2, min_value)
            pi.set_servo_pulsewidth(ESC3, min_value)
            pi.set_servo_pulsewidth(ESC4, min_value)
ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
norm = 1040
pi.set_servo_pulsewidth(ESC1, norm)
pi.set_servo_pulsewidth(ESC2, norm)
pi.set_servo_pulsewidth(ESC3, norm)
pi.set_servo_pulsewidth(ESC4, norm)

i =0;
while(True):
    set = 1030
    line =ser.readline()
    if(len(line) ==0 or i<10):
        i+=1
        continue
    line=line.split("\t")
    if(abs(int(line[0]))>abs(int(line[1])) & abs(int(line[0]))>abs(int(line[2]))):
        if(int(line[0])>0):
            pi.set_servo_pulsewidth(ESC1,set+100)
            pi.set_servo_pulsewidth(ESC2,set+100)
            pi.set_servo_pulsewidth(ESC3, 1030)
            pi.set_servo_pulsewidth(ESC4, 1030)
        else:
            pi.set_servo_pulsewidth(ESC3,set+100)
            pi.set_servo_pulsewidth(ESC4,set+100)
            pi.set_servo_pulsewidth(ESC1, 1030)
            pi.set_servo_pulsewidth(ESC2, 1030)
    if(abs(int(line[1]))>abs(int(line[0])) & abs(int(line[1]))>abs(int(line[2]))):
        if(int(line[1])>0):
            pi.set_servo_pulsewidth(ESC1,1030)
            pi.set_servo_pulsewidth(ESC2,1030+100)
            pi.set_servo_pulsewidth(ESC3, 1030+100)
            pi.set_servo_pulsewidth(ESC4, 1030)
        else:
            pi.set_servo_pulsewidth(ESC3,set+100)
            pi.set_servo_pulsewidth(ESC4,set)
            pi.set_servo_pulsewidth(ESC1, 1030)
            pi.set_servo_pulsewidth(ESC2, 1030+100)
    
