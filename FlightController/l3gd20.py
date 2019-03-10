import adafruit_l3gd20

from busio import I2C
from board import SDA, SCL

i2c = I2C(SCL, SDA)

sensor = adafruit_l3gd20.L3GD20_I2C(i2c)

while(True):
    print(sensor.gyro)
