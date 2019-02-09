import os
import serial
import time
os.system("sudo pigpiod") #Launching GPIO library
time.sleep(1)
import pigpio
import sys
import program

#////////////////////////////////MOTOR SETUP///////////////////////////////////
ESC1=13  #ESC connections with the GPIO pins; note its the BROADCOM number, not the GPIO pin number!
ESC2=12
ESC3=18
ESC4=19

#max 1400, min 1030
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

#ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
norm = 1040
pi.set_servo_pulsewidth(ESC1, norm)
pi.set_servo_pulsewidth(ESC2, norm)
pi.set_servo_pulsewidth(ESC3, norm)
pi.set_servo_pulsewidth(ESC4, norm)
#//////////////////////////////////////////////////////////////////////////////////


#Setup variables
rad_to_deg = 180/3.141592654
imu = program.init()
timeV = time.time()
previous_errorP, previous_errorR = 0.0

#PID Constants:
kp=1
ki=1
kd=1

desired_angle = 0

while(True):
    timePrev=timeV
    timeV=time.time()
    elapsedTime = (timeV - timePrev)/1000

    angle = program.angle(imu)#Pitch, Roll

    errorP = angle[0]-desired_angle
    errorR = angle[1]-desired_angle

    Ppid_p = kp*errorP
    Rpid_p = kp*errorR

    if abs(errorP) < 3:
        Ppid_i = Ppid_i + (ki*errorP)
    if abs(errorR) < 3:
        Rpid_i = Rpid_i + (ki*errorR)
        

    Ppid_d = kd*((errorP - previous_errorP)/elapsedTime)
    Rpid_d = kd*((errorR - previous_errorR)/elapsedTime)

    PPID = Ppid_p + Ppid_i + Ppid_d
    RPID = Rpid_p + Rpid_i + Rpid_d

    
    if PPID < -370:
        PPID = -370
    elif PPID > 370:
        PPID = 370

    if RPID < -370:
        RPID = -370
    elif RPID > 370:
        RPID = 370
        

    PBack = norm + PPID
    PFront = norm - PPID
    
    RLeft = norm + RPID
    RRight = norm - RPID

    
    if PBack > 1400:
        PBack = 1400
    elif PBack < 1030:
        PBack = 1030
        
    if PFront > 1400:
        PFront = 1400
    elif PFront < 1030:
        PFront = 1030

        
    if RLeft > 1400:
        RLeft = 1400
    elif RLeft < 1030:
        RLeft = 1030
        
    if RRight > 1400:
        RRight = 1400
    elif RRight < 1030:
        RRight = 1030
        
    pi.set_servo_pulsewidth(ESC1, (PBack+RRight)/2)
    pi.set_servo_pulsewidth(ESC2, (PFront+RRight)/2)
    pi.set_servo_pulsewidth(ESC3, (PFront+RLeft)/2)
    pi.set_servo_pulsewidth(ESC4, (PBack+RLeft)/2)
    
    previous_errorP = errorP
    previous_errorR = errorR

        
