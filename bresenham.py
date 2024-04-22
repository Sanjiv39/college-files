from graphics import *

def draw_line_bresenham(x1, y1, x2, y2, win):
    # Calculate the differences between the coordinates
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Calculate the increments
    dx2 = 2 * dx
    dy2 = 2 * dy
    
    # Determine the direction of the line
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    
    # Initial coordinates
    x = x1
    y = y1
    
    # Check the slope to decide the initial decision parameter
    if dx >= dy:
        # Decision parameter for x
        decision = dy2 - dx
        while x != x2:
            Point(x, y).draw(win)
            if decision >= 0:
                y += sy
                decision -= dx2
            x += sx
            decision += dy2
    else:
        # Decision parameter for y
        decision = dx2 - dy
        while y != y2:
            Point(x, y).draw(win)
            if decision >= 0:
                x += sx
                decision -= dy2
            y += sy
            decision += dx2
            
    Point(x, y).draw(win)

def main():
    # Create a new window
    win = GraphWin("Bresenham’s Line Drawing Algorithm", 400, 400)
    
    # Get the coordinates from the user
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    
    # Draw the line using Bresenham’s algorithm
    draw_line_bresenham(x1, y1, x2, y2, win)
    
    # Wait for the user to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
