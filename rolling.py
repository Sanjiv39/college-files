from graphics import *

# Create a window
win = GraphWin("Rolling Ball Animation", 500, 500)

# Set initial position and velocity
x = 250
y = 250
velocity_x = 2
velocity_y = 2
radius = 20

# Create a ball
ball = Circle(Point(x, y), radius)
ball.setFill("blue")
ball.draw(win)

# Animation loop
while True:
    # Move the ball
    ball.move(velocity_x, velocity_y)
    
    # Update position
    x += velocity_x
    y += velocity_y
    
    # Reverse direction if the ball hits the window borders
    if x - radius <= 0 or x + radius >= 500:
        velocity_x = -velocity_x
    if y - radius <= 0 or y + radius >= 500:
        velocity_y = -velocity_y
    
    # Delay to control animation speed
    time.sleep(0.01)
    
    # Update the window
    win.update()

# Close the window on click
win.getMouse()
win.close()
