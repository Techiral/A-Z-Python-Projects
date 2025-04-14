import turtle

# Function to draw a Sierpinski triangle
def sierpinski(order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        size /= 2
        sierpinski(order - 1, size)
        turtle.forward(size)
        sierpinski(order - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        sierpinski(order - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)

# Initialize the Turtle
turtle.speed(0)  # Fastest drawing speed
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()

# Set the order and size of the Sierpinski triangle
order = 3  # You can adjust this to change the level of detail
size = 300

# Draw the Sierpinski triangle
sierpinski(order, size)

# Close the Turtle graphics window on click
turtle.exitonclick()
