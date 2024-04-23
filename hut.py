from graphics import *

# Create a graphics window
win = GraphWin("Simple Hut", 400, 400)

# Draw the hut base
base = Rectangle(Point(100, 300), Point(300, 200))
base.setFill("brown")
base.draw(win)

# Draw the hut roof
roof = Polygon(Point(100, 200), Point(300, 200), Point(200, 100))
roof.setFill("red")
roof.draw(win)

# Draw the door
door = Rectangle(Point(180, 300), Point(220, 250))
door.setFill("brown")
door.draw(win)

# Draw the window
window = Rectangle(Point(130, 270), Point(170, 230))
window.setFill("lightblue")
window.draw(win)

# Draw the sun
sun = Circle(Point(350, 50), 30)
sun.setFill("yellow")
sun.draw(win)

# Keep the window open until closed by the user
win.mainloop()
