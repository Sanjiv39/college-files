from graphics import *

# Create a graphics window
win = GraphWin("Coordinate Axis", 400, 400)

# Calculate the center coordinates of the window
center_x = win.getWidth() // 2
center_y = win.getHeight() // 2

# Draw the x-axis
x_axis = Line(Point(0, center_y), Point(win.getWidth(), center_y))
x_axis.setFill("black")
x_axis.setWidth(2)
x_axis.draw(win)

# Draw the y-axis
y_axis = Line(Point(center_x, 0), Point(center_x, win.getHeight()))
y_axis.setFill("black")
y_axis.setWidth(2)
y_axis.draw(win)

# Keep the window open until closed by the user
win.mainloop()
