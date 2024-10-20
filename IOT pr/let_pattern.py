# let pattern
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.Board)
GPIO.setup(3,GPIO.OUT)
while True:
    GPIO.output(3,True)
    time.sleep(1)
    GPIO.output(3,False)
    time.sleep(1)
