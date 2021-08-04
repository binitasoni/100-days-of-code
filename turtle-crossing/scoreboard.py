FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-270,270)
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=0
        self.update()
        self.clear()

    def update(self):
        self.clear()
        self.level = self.level+1
        self.write(f"Level:{self.level}",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game over", font=FONT)
