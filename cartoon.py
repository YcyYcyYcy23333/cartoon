from turtle import *

def draw_happy_face():
    speed(10)  # Set the drawing speed
    bgcolor("lightblue")  # Set the background color
    pensize(5)  # Set pen size

    # Draw the face
    penup()
    goto(0, -100)  # Move to the center bottom
    pendown()
    color("yellow")  # Face color
    begin_fill()
    circle(100)  # Draw face as a circle
    end_fill()

    # Draw the eyes
    # Left eye
    penup()
    goto(-35, 20)  # Position for left eye
    pendown()
    color("black")  # Eye color
    begin_fill()
    circle(10)  # Draw left eye
    end_fill()

    # Right eye
    penup()
    goto(35, 20)  # Position for right eye
    pendown()
    begin_fill()
    circle(10)  # Draw right eye
    end_fill()

    # Draw the mouth
    penup()
    goto(-40, -20)  # Move to mouth position
    seth(-60)  # Set heading
    pendown()
    color("black")  # Mouth color
    begin_fill()
    circle(40, 120)  # Draw the mouth as a curve
    end_fill()

    # Draw the smile
    penup()
    goto(-40, -20)  # Reset to mouth position
    seth(-60)  # Set heading
    pendown()
    color("red")  # Smile color
    circle(40, -120)  # Draw the smile

    # Finish
    penup()
    goto(0, -150)  # Move to a suitable position to finish
    pendown()

# Run the function to draw
draw_happy_face()
done()

