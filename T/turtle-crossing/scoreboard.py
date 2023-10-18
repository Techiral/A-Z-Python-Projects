from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
