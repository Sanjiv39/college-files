import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False) 
reader = SimpleMFRC522() 

while True: 
    try: 
        id, text = reader.read()
        print(id)
        print(text) 
    finally: 
        GPIO.cleanup()
    sleep(0.5)