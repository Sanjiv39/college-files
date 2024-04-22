from graphics import *
win = GraphWin("Scale Square", 600, 600)

# Original
x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
c1=Point(x1, y1)
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))
c2 = Point(x2, y2)
s = Rectangle(c1, c2)
s.draw(win)
s.setFill("blue")

# Scaling
sx=float(input("Scaling Factor sx : "))
sy=float(input("Scaling Factor sy : "))
x1*=sx
x2*=sx
y1*=sy
y2*=sy
c1 = Point(x1, y1)
c2 = Point(x2, y2)
ss=Rectangle(c1, c2)
ss.draw(win)
ss.setFill("green")
win.getMouse()
win.close()