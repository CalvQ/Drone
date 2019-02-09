import RPi.GPIO as IO
import time                            #calling time to provide delays in program
IO.setwarnings(False)           #do not show any warnings
IO.setmode (IO.BCM)
IO.setup(19,IO.OUT)           # initialize GPIO19 as an output.
p = IO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle

while 1:                               #execute loop forever

        for x in range (50):                          #execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
            time.sleep(0.1)                           #sleep for 100m second
            
        for x in range (50):                         #execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(50-x)        #change duty cycle for changing the brightness of LED.
            time.sleep(0.1)                          #sleep for 100m second
