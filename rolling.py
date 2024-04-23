from graphics import *
import time
import math

def draw_ball(win, x, y, radius):
    ball = Circle(Point(x, y), radius)
    ball.setFill("red")
    ball.setOutline("black")
    ball.setWidth(2)
    ball.draw(win)
    return ball

def roll_ball(win, ball, start_x, start_y, end_x, end_y, radius):
    distance = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
    steps = int(distance / radius) * 2
    dx = (end_x - start_x) / steps
    dy = (end_y - start_y) / steps

    for _ in range(steps):
        ball.move(dx, dy)
        time.sleep(0.05)

def main():
    # Create a graphics window
    win = GraphWin("Rolling Ball Animation", 400, 400)

    # Initial ball position and size
    start_x = 50
    start_y = 50
    end_x = 350
    end_y = 350
    radius = 20

    # Draw the ball
    ball = draw_ball(win, start_x, start_y, radius)

    # Roll the ball to the end position
    roll_ball(win, ball, start_x, start_y, end_x, end_y, radius)

    # Close the window on click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
