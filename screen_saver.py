from graphics import *
import random, time
win = GraphWin("Random Circles", 300, 300)

for i in range(100):
    r = random.randrange(250)
    b = random.randrange(250)
    g = random.randrange(250)
    color = color_rgb(r, b, g)
    a = random.randrange(10)
    x = random.randrange(250)
    y = random.randrange(250)
    p = Point(x,y)
    
    txt = Text(p,"hello")
    txt.setTextColor(color)
    txt.setSize(30)
    txt.setFace('courier')
    txt.draw(win)
    time.sleep(1.0)
    txt.undraw()