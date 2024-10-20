import tm1637
import time
from datetime import datetime

# Create an instance of the TM1637 display
tm = tm1637.TM1637(clk=18, dio=17)
clear = [0, 0, 0, 0]
tm.write(clear) 
time.sleep(1)

s = 'This is pretty cool'
tm.scroll(s, delay=250)
time.sleep(1)  

# Clear the display again
tm.write(clear)
time.sleep(1)

# Main loop to display current time
while True:
    now = datetime.now() 
    hh = int(now.strftime('%H'))  # Get current hour
    mm = int(now.strftime('%M'))  # Get current minute

    # Display the current time on the TM1637
    tm.numbers(hh, mm, colon=True)
    time.sleep(1)  # Update every second
