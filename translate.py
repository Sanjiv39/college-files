from graphics import *

def translate_shape(shape, tx, ty):
    for p in shape:
        p.move(tx, ty)

def main():
    # Create a new window
    win = GraphWin("2D Translation", 400, 400)
    
    # Create the original shape
    shape = [Point(100, 100), Point(100, 200), Point(200, 200), Point(200, 100)]
    polygon = Polygon(shape)
    polygon.setFill("blue")
    polygon.draw(win)
    
    # Get the translation distances from the user
    tx = int(input("Enter translation distance in x direction: "))
    ty = int(input("Enter translation distance in y direction: "))
    
    # Translate the shape
    translate_shape(shape, tx, ty)
    translated = Polygon(shape)
    translated.setFill("green")
    translated.draw(win)
    
    # Wait for the user to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
