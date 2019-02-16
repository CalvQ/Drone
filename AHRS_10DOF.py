import adafruit_l3gd20
import adafruit_lsm303

import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)

gyro = adafruit_l3gd20.L3GD20_I2C(i2c)
accel = adafruit_lsm303.LSM303(i2c)

timeV = time.time()


while(True):
    #f = open("data", "w")
    #f.write(

    acceleration = accel.acceleration() # x,y,z in M/s
    magneto = accel.magnetic() # x,y,z in mT
    angle = gyro.gyro() # x,y,z angular momentum

    print(acceleration + " " + magneto + " " + angle)

    timePrev=timeV
    timeV=time.time()
    elapsedTime = (timeV - timePrev)/1000

    
