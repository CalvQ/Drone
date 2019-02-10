

import FaBo9Axis_MPU9250
import time
import sys
import math
#mpu9250 = FaBo9Axis_MPU9250.MPU9250()

def init():
    mpu9250 = FaBo9Axis_MPU9250.MPU9250()
    return mpu9250

def angle(mpu9250):

        accel = mpu9250.readAccel()
        #print " ax = " , ( accel['x'] )
        #print " ay = " , ( accel['y'] )
        #print " az = " , ( accel['z'] )
        gyro = mpu9250.readGyro()
        #print " gx = " , ( gyro['x'] )
        #print " gy = " , ( gyro['y'] )
        #print " gz = " , ( gyro['z'] )

        mag = mpu9250.readMagnet()
        #print " mx = " , ( mag['x'] )
        #print " my = " , ( mag['y'] )
        #print " mz = " , ( mag['z'] )
        #print
        Acceleration_angle = [0,0]
        Acceleration_angle[0] = math.atan((accel['y'])/math.sqrt(pow(accel['x'],2) + pow(accel['z'],2)))*180/3.141592654;
        Acceleration_angle[1] = math.atan(-1*accel['x']/math.sqrt(pow(accel['y'],2) + pow(accel['z'],2)))*180/3.141592654;
        return Acceleration_angle
#mpu9250=init()
#angle(mpu9250)

'''
try:
    while True:
        accel = mpu9250.readAccel()
        #print " ax = " , ( accel['x'] )
        #print " ay = " , ( accel['y'] )
        #print " az = " , ( accel['z'] )
        gyro = mpu9250.readGyro()
        #print " gx = " , ( gyro['x'] )
        #print " gy = " , ( gyro['y'] )
        #print " gz = " , ( gyro['z'] )

        mag = mpu9250.readMagnet()
        #print " mx = " , ( mag['x'] )
        #print " my = " , ( mag['y'] )
        #print " mz = " , ( mag['z'] )
        #print
        Acceleration_angle = [0,0]
        Acceleration_angle[0] = math.atan((accel['y'])/math.sqrt(pow(accel['x'],2) + pow(accel['z'],2)))*180/3.141592654;
        Acceleration_angle[1] = math.atan(-1*accel['x']/math.sqrt(pow(accel['y'],2) + pow(accel['z'],2)))*180/3.141592654;
        print Acceleration_angle
        time.sleep(0.1)


#except KeyboardInterrupt:
#    sys.exit()
'''
