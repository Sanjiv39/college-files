from graphics import *
import random, time

win = GraphWin("Random Circles", 300, 300)

for circle in range(100):

    r = random.randrange(250)
    b = random.randrange(250)
    g = random.randrange(250)
    color = color_rgb(r, b, g)

    #creating circle objects with different radius
    radius = random.randrange(3, 12)
    x = random.randrange(5, 295)
    y = random.randrange(5, 295)
    circle = Circle(Point(x,y), radius)

    #painting circle objects with different colors
    circle.setFill(color)
    circle.draw(win)

    #time taken for each circle object to appear
    time.sleep(.05)