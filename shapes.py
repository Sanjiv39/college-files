from graphics import *
def main():
    win = GraphWin('My Graphics', 300, 300) # specifies graphics window size 250x250
    g = Point(200,100)# creates a Point object at x=125 y=125
    g.setOutline('red')
    g.draw(win) # draws to the graphics window
    cir = Circle(Point(250,250), 20)
    cir.draw(win)
    cir.setOutline('blue')
    cir.setFill('pink')
    txt= Text (Point (200, 200), "hello")
    txt.setTextColor (color_rgb(0, 255, 200))
    txt.setSize(30)
    txt. setFace('courier')
    txt.draw(win)
    line = Line(Point(100, 50), Point(150, 100))
    line.setOutline('red')
    line.move(20,40)
    line.draw(win)
    pt = Point(50, 50)
    rect = Rectangle(Point (20, 10), pt)
    rect.setOutline('red')
    rect.setFill('pink')
    rect.draw(win)
    oval = Oval(Point (20, 100), Point (70, 120))
    oval.setFill('pink')
    oval.draw(win)
    tri = Polygon(Point(25, 25), Point(175, 100), Point(25, 175))
    tri.draw(win)
    win.getMouse() # keep window up
    win.close()
main()