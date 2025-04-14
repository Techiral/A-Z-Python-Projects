from turtle import Turtle, Screen
from math import pi, sin, cos
from random import randint, random

RADIUS = 180  # roughly the radius of a completed spiral

screen = Screen()
screen.title("Archimedes' Spiral")

WIDTH, HEIGHT = screen.window_width(), screen.window_height()

t = Turtle(visible=False)
t.speed('fastest')  # because I have no patience

t.up()

for _ in range(3):
    x = randint(RADIUS - WIDTH//2, WIDTH//2 - RADIUS)
    y = randint(RADIUS - HEIGHT//2, HEIGHT//2 - RADIUS)
    t.goto(x, y)

    t.color(random(), random(), random())
    t.down()

    for i in range(200):
        t_ = i / 20 * pi
        dx = (1 + 5 * t_) * cos(t_)
        dy = (1 + 5 * t_) * sin(t_)

        t.goto(x + dx, y + dy)

    t.up()

screen.exitonclick()
