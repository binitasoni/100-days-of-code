from turtle import Turtle
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.l=0
        self.r=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l}", move=False, align="left", font=("Arial", 30, "normal"))
        self.goto(100,200)
        self.write(f"{self.r}", move=False, align="left", font=("Arial", 30, "normal"))
    def l__score(self):
        self.l=self.l+1
    def r__score(self):
        self.r=self.r+1

