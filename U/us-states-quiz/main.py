import turtle
from turtle import Screen, Turtle

import pandas

screen = Screen()
my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.penup()
screen.title("U.S. state game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()
answered_states = []

while len(answered_states) < len(all_states):
    ans_state = turtle.textinput(f"{len(answered_states)}/{len(all_states)} answered correct",
                                 prompt="What's another state's name?").title()

    if ans_state == "Exit":
        break
    if ans_state in all_states:
        answered_states.append(ans_state)
        state_row = states_data[states_data["state"] == ans_state]
        row = state_row.iloc[0]
        my_turtle.goto(row['x'], row['y'])
        my_turtle.write(ans_state)

