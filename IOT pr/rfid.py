import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522 
GPIO.setwarnings(False) 
SimpleMFRC522() 
while True: 
   """try: 
     id, text = reader.read() 
     print(id) 
     print(text) 
    finally:
      GPIO.cleanup()"""