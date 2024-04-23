from graphics import *

def draw_circle_midpoint(xc, yc, r, win):
    x = 0
    y = r
    p = 1 - r
    
    plot_circle_points(xc, yc, x, y, win)
    
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, win)

def plot_circle_points(xc, yc, x, y, win):
    Point(xc + x, yc + y).draw(win)
    Point(xc - x, yc + y).draw(win)
    Point(xc + x, yc - y).draw(win)
    Point(xc - x, yc - y).draw(win)
    Point(xc + y, yc + x).draw(win)
    Point(xc - y, yc + x).draw(win)
    Point(xc + y, yc - x).draw(win)
    Point(xc - y, yc - x).draw(win)

def main():
    # Create a new window
    win = GraphWin("Mid-Point Circle Drawing Algorithm", 400, 400)
    
    # Get the center and radius from the user
    xc = int(input("Enter x coordinate of the center: "))
    yc = int(input("Enter y coordinate of the center: "))
    r = int(input("Enter the radius of the circle: "))
    
    # Draw the circle using Mid-Point algorithm
    draw_circle_midpoint(xc, yc, r, win)
    
    # Wait for the user to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
