from graphics import *
import time

def draw_face(win):
    # Draw face circle
    face = Circle(Point(200, 200), 80)
    face.setFill("yellow")
    face.setOutline("black")
    face.setWidth(2)
    face.draw(win)

    # Draw left eye
    left_eye = Circle(Point(170, 170), 10)
    left_eye.setFill("white")
    left_eye.draw(win)

    # Draw right eye
    right_eye = Circle(Point(230, 170), 10)
    right_eye.setFill("white")
    right_eye.draw(win)

    # Draw left eye pupil
    left_pupil = Circle(Point(170, 170), 5)
    left_pupil.setFill("black")
    left_pupil.draw(win)

    # Draw right eye pupil
    right_pupil = Circle(Point(230, 170), 5)
    right_pupil.setFill("black")
    right_pupil.draw(win)

    # Draw mouth
    mouth = Oval(Point(170, 230), Point(230, 250))
    mouth.setWidth(2)
    mouth.draw(win)

    return left_pupil, right_pupil, mouth

def smile_animation(win, left_pupil, right_pupil, mouth):
    # for _ in range(3):
    #     # Move pupils up to make the eyes appear closed
    #     for _ in range(10):
    #         left_pupil.move(0, -1)
    #         right_pupil.move(0, -1)
    #         time.sleep(0.05)

    #     # Move pupils down to make the eyes appear open
    #     for _ in range(10):
    #         left_pupil.move(0, 1)
    #         right_pupil.move(0, 1)
    #         time.sleep(0.05)

    # Animate the smile
    for _ in range(3):
        # Make the smile larger
        for _ in range(10):
            mouth.move(0, -1)
            time.sleep(0.05)

        # Make the smile smaller
        for _ in range(10):
            mouth.move(0, 1)
            time.sleep(0.05)

def main():
    # Create a graphics window
    win = GraphWin("Smiling Face Animation", 400, 400)

    # Draw the face
    left_pupil, right_pupil, mouth = draw_face(win)

    # Start the smile animation
    smile_animation(win, left_pupil, right_pupil, mouth)

    # Close the window on click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
