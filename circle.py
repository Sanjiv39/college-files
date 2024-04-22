from graphics import *
import time
import math

def draw_clock():
    # Create a new window
    win = GraphWin("Simple Clock", 400, 400)
    
    # Calculate the center point of the window
    center = Point(200, 200)
    
    # Draw the clock face
    Circle(center, 180).draw(win)
    
    # Draw the hour hand
    hour_hand = Line(center, Point(200, 110))
    hour_hand.setWidth(5)
    hour_hand.setFill("blue")
    hour_hand.draw(win)
    
    # Draw the minute hand
    minute_hand = Line(center, Point(200, 70))
    minute_hand.setWidth(3)
    minute_hand.setFill("red")
    minute_hand.draw(win)
    
    # Draw the second hand
    second_hand = Line(center, Point(200, 50))
    second_hand.setWidth(1)
    second_hand.setFill("green")
    second_hand.draw(win)
    
    return win, hour_hand, minute_hand, second_hand

def update_clock(hour_hand, minute_hand, second_hand):
    hour_hand.undraw()
    minute_hand.undraw()
    second_hand.undraw()

    # Get the current time
    current_time = time.localtime()
    
    # Update the hour hand
    hour_angle = math.radians((current_time.tm_hour % 12) * 30)
    hour_hand = Line(Point(200, 200), Point(200 + 80 * math.cos(hour_angle), 200 + 80 * math.sin(hour_angle)))
    hour_hand.setWidth(5)
    hour_hand.setFill("blue")
    hour_hand.draw(win)
    
    # Update the minute hand
    minute_angle = math.radians(current_time.tm_min * 6 - 90)
    minute_hand = Line(Point(200, 200), Point(200 + 130 * math.cos(minute_angle), 200 + 130 * math.sin(minute_angle)))
    minute_hand.setWidth(3)
    minute_hand.setFill("red")
    minute_hand.draw(win)
    
    # Update the second hand
    second_angle = math.radians(current_time.tm_sec * 6 - 90)
    second_hand = Line(Point(200, 200), Point(200 + 140 * math.cos(second_angle), 200 + 140 * math.sin(second_angle)))
    second_hand.setWidth(1)
    second_hand.setFill("green")
    second_hand.draw(win)

# Create the clock
win, hour_hand, minute_hand, second_hand = draw_clock()

# Update the clock every second
while True:
    update_clock(hour_hand, minute_hand, second_hand)
    time.sleep(1)

# Close the window
win.getMouse()
win.close()
