import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# pins for led output
r= [3,15,8,11,13,26,29,22]
GPIO.setup(r, GPIO.OUT)

while True:
    for i in r:
        GPIO.output(i, GPIO.HIGH)
        sleep (0.1)
        GPIO.output(i, GPIO.LOW) 
        sleep (0.1)