from graphics import *

def draw_line_dda(x1, y1, x2, y2, win):
    # Calculate the differences between the coordinates
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate the number of steps needed
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    # Calculate the increment values for x and y
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    
    # Initialize starting coordinates
    x = x1
    y = y1
    
    # Draw the starting point
    Point(round(x), round(y)).draw(win)
    
    # Draw the line
    for _ in range(steps):
        x += x_increment
        y += y_increment
        Point(round(x), round(y)).draw(win)

def main():
    # Create a new window
    win = GraphWin("DDA Line Drawing Algorithm", 400, 400)
    
    # Get the coordinates from the user
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    
    # Draw the line using DDA algorithm
    draw_line_dda(x1, y1, x2, y2, win)
    
    # Wait for the user to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
