import turtle

def koch_snowflake(order, size, t):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(order - 1, size / 3, t)
            t.left(angle)

def draw_koch_snowflake(order, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Koch Snowflake")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()
    
    for _ in range(3):
        koch_snowflake(order, size, t)
        t.right(120)
    
    screen.exitonclick()

def main():
    order = 5  # Adjust the order to change the complexity of the snowflake
    size = 300  # Adjust the initial size of the snowflake
    
    draw_koch_snowflake(order, size)

if __name__ == "__main__":
    main()
