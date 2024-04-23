from graphics import *
import time

def draw_car(win, x, y):
    # Draw car body
    body = Rectangle(Point(x, y), Point(x + 100, y + 40))
    body.setFill("blue")
    body.draw(win)

    # Draw car roof
    roof = Polygon(Point(x + 10, y), Point(x + 90, y), Point(x + 80, y - 20), Point(x + 20, y - 20))
    roof.setFill("blue")
    roof.draw(win)

    # Draw wheels
    wheel1 = Circle(Point(x + 25, y + 40), 10)
    wheel1.setFill("black")
    wheel1.draw(win)

    wheel2 = Circle(Point(x + 75, y + 40), 10)
    wheel2.setFill("black")
    wheel2.draw(win)

    return body, roof, wheel1, wheel2

def move_car(win, body, roof, wheel1, wheel2):
    for _ in range(10):
        # Move the car to the right
        body.move(10, 0)
        roof.move(10, 0)
        wheel1.move(10, 0)
        wheel2.move(10, 0)
        time.sleep(0.1)

    # Reset car position
    body.move(-1000, 0)
    roof.move(-1000, 0)
    wheel1.move(-1000, 0)
    wheel2.move(-1000, 0)

def main():
    # Create a graphics window
    win = GraphWin("Moving Car", 600, 400)

    # Initial car position
    x = -100
    y = 200

    # Draw the car
    body, roof, wheel1, wheel2 = draw_car(win, x, y)

    # Move the car across the screen
    for _ in range(3):
        move_car(win, body, roof, wheel1, wheel2)

    # Close the window on click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
