from time import sleep
from picamera import PiCamera

# Create an instance of the PiCamera
camera = PiCamera()

# Set the camera resolution
camera.resolution = (1280, 720)

# Start the camera preview
camera.start_preview()
sleep(0.5)  # Give the camera time to adjust to lighting

# Capture an image and save it
camera.capture('/home/sahyog123/Pictures/new1.jpg')

# Stop the camera preview
camera.stop_preview()
