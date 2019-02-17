import importlib.util
specG = importlib.util.spec_from_file_location("adafruit_l3gd20", "../Adafruit_CircuitPython_Bundle/libraries/drivers/l3gd20/adafruit_l3gd20.py")
specA = importlib.util.spec_from_file_location("adafruit_lsm303", "../Adafruit_CircuitPython_Bundle/libraries/drivers/lsm303/adafruit_lsm303.py")
#import adafruit-circuitpython-l3gd20 as l3gd
#import adafruit-circuitpython-lsm303 as lsm

l3gd = importlib.util.module_from_spec(specG)
lsm = importlib.util.module_from_spec(specA)

specG.loader.exec_module(l3gd)
specA.loader.exec_module(lsm)

import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)

gyro = l3gd.L3GD20_I2C(i2c)
accel = lsm.LSM303(i2c)

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

    
