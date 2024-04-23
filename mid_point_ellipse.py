from graphics import *

def drawEllipse(win, xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = ry**2 - (rx**2 * ry) + (0.25 * rx**2)

    plotEllipsePoints(win, xc, yc, x, y)
    
    while (2 * ry**2 * x) < (2 * rx**2 * y):
        x += 1
        if p1 < 0:
            p1 += 2 * ry**2 * x + ry**2
        else:
            y -= 1
            p1 += 2 * ry**2 * x - 2 * rx**2 * y + ry**2
        plotEllipsePoints(win, xc, yc, x, y)

    p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)

    while y > 0:
        y -= 1
        if p2 > 0:
            p2 += rx**2 - 2 * rx**2 * y
        else:
            x += 1
            p2 += 2 * ry**2 * x - 2 * rx**2 * y + rx**2
        plotEllipsePoints(win, xc, yc, x, y)

def plotEllipsePoints(win, xc, yc, x, y):
    win.plotPixel(xc + x, yc + y, "black")
    win.plotPixel(xc - x, yc + y, "black")
    win.plotPixel(xc + x, yc - y, "black")
    win.plotPixel(xc - x, yc - y, "black")

# Create a graphics window
win = GraphWin("Midpoint Ellipse Drawing Algorithm", 400, 400)

# Center coordinates and radii of the ellipse
xc = win.getWidth() // 2
yc = win.getHeight() // 2
rx = 100
ry = 50

# Draw the ellipse
drawEllipse(win, xc, yc, rx, ry)

# Keep the window open until closed by the user
win.mainloop()
