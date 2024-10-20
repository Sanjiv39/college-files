import Rpi.GPIO as GPIO
GPIO.setmode(GPIO.Board)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,True)

