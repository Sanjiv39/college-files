import RPi.GPIO as GPIO  # Import the RPi.GPIO library to control GPIO pins
import telebot

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
bot = telebot.TeleBot(token, parse_mode=None)
print('Started.....')

colors = ["blue", "yellow", "red"]

def msg_handler(msg = "", on = False):
    output = 1 if on else 0
    strings = []
    if 'all' in msg:
        for a in colors:
                strings.append(a)
        GPIO.output(blue, output)
        GPIO.output(yellow, output)
        GPIO.output(red, output)
    else:
        if colors[0] in msg:
            strings.append("blue")
            GPIO.output(blue, output)
        if colors[1] in msg:
            strings.append("yellow")
            GPIO.output(yellow, output)
        if colors[2] in msg:
            strings.append("red")
            GPIO.output(red, output)
    return strings


# Define a function to handle incoming Telegram messages
@bot.message_handler(commands=['on', 'off'])
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % command)
    
    # Check for 'on' command and control LEDs accordingly
    if '/on' in command:
        colors = msg_handler(command, True)
        string = f"Turned on {' '.join(colors)}"
        bot.reply_to(msg, string)

    # Check for 'off' command and turn off LEDs accordingly
    elif '/off' in command:
        colors = msg_handler(command, True)
        string = f"Turned off {' '.join(colors)}"
        bot.reply_to(msg, string)


# Start the polling to listen for incoming Telegram messages
bot.infinity_polling()
