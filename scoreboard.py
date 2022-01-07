from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level=1
        self.color("black")
        self.goto(-280,270)
        self.hideturtle()
    def update_score(self):
        self.write(f"Level = {self.level}",align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
    def increase_score(self):
        self.level+=1
        self.clear()