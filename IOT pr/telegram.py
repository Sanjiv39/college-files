import RPi.GPIO as GPIO  # Import the RPi.GPIO library to control GPIO pins
import telepot  # Import the telepot library for Telegram bot functionality
from telepot.loop import MessageLoop  # Import MessageLoop to handle Telegram messages
import time  # Import time for sleep functionality

# Set up GPIO mode and suppress warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO pin numbers for the LEDs
blue = 7
red = 11
yellow = 13

# Set up GPIO pins as outputs and turn them off
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, False)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, False)
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, False)

# Initialize the Telegram bot with your token
telegram_bot = telepot.Bot('Your-Telegram-Bot-Token-Goes-Here')
print('Up and Running…')

# Define a function to handle incoming Telegram messages
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % command)
    message = ''
    
    # Check for 'on' command and control LEDs accordingly
    if 'on' in command:
        if 'blue' in command:
            message += " blue"
            GPIO.output(blue, 1)
        if 'yellow' in command:
            message += " yellow"
            GPIO.output(yellow, 1)
        if 'red' in command:
            message += " red"
            GPIO.output(red, 1)
        if 'all' in command:
            message += " all"
            GPIO.output(blue, 1)
            GPIO.output(yellow, 1)
            GPIO.output(red, 1)

        message += " lights"
        telegram_bot.sendMessage(chat_id, message)

    # Check for 'off' command and turn off LEDs accordingly
    elif 'off' in command:
        message = 'off'
        if 'blue' in command:
            message += " blue"
            GPIO.output(blue, 0)
        if 'yellow' in command:
            message += " yellow"
            GPIO.output(yellow, 0)
        if 'red' in command:
            message += " red"
            GPIO.output(red, 0)
        if 'all' in command:
            message += " all"
            GPIO.output(blue, 0)
            GPIO.output(yellow, 0)
            GPIO.output(red, 0)

        message += " lights"
        telegram_bot.sendMessage(chat_id, message)

# Start the MessageLoop to listen for incoming Telegram messages
MessageLoop(telegram_bot, action).run_as_thread()

# Keep the script running while True
while True:
    time.sleep(10)  # Sleep for 10 seconds to avoid excessive CPU usage
