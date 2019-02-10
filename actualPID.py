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

#max 1400, min 600
max_value = 1500
min_value = 970
pi = pigpio.pi();
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


#Setup variables
rad_to_deg = 180/3.141592654
#imu = program.init()
timeV = time.time()
previous_errorP = 0.0
previous_errorR = 0.0
Ppid_i = 0.0
Rpid_i = 0.0
#PID Constants:
kp=3
ki=0.015
kd=2.05

desired_angle = 0

while(True):
    timePrev=timeV
    timeV=time.time()
    elapsedTime = (timeV - timePrev)/1000

    f = open("data.txt","r")
    a = f.readline()
    f.close()
    strA = a.split(",")
    try:
        strA[0] =float(strA[0])
        strA[1] = float(strA[1])
    except:
        continue
    print strA
    #angle = program.angle(*)

    errorP = strA[0]-desired_angle
    errorR = strA[1]-desired_angle

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

    
    if PPID < -800:
        PPID = -800
    elif PPID > 800:
        PPID = 800

    if RPID < -800:
        RPID = -800
    elif RPID > 800:
        RPID = 800
        

    PBack = norm + PPID
    PFront = norm - PPID
    
    RLeft = norm + RPID
    RRight = norm - RPID

    
    if PBack > 1400:
        PBack = 1400
    elif PBack < 600:
        PBack = 600
        
    if PFront > 1400:
        PFront = 1400
    elif PFront < 600:
        PFront = 600

        
    if RLeft > 1400:
        RLeft = 1400
    elif RLeft < 600:
        RLeft = 600
        
    if RRight > 1400:
        RRight = 1400
    elif RRight < 600:
        RRight = 600


    pi.set_servo_pulsewidth(ESC1, (PBack+RRight)/2)
    pi.set_servo_pulsewidth(ESC2, (PFront+RRight)/2)
    pi.set_servo_pulsewidth(ESC3, (PFront+RLeft)/2)
    pi.set_servo_pulsewidth(ESC4, (PBack+RLeft)/2)
    
    #print PBack+RLeft

    if (PBack+RLeft)/2 > (PFront+RLeft)/2:
        print "Back------------------------------------------"
    else:
        print "Front"

    previous_errorP = errorP
    previous_errorR = errorR
    time.sleep(0.3)
        
