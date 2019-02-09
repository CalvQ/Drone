from gpiozero import PWMOutputDevice
from time import sleep

motor1 = PWMOutputDevice(19, True,0.8 ,50)
sleep(1000)
