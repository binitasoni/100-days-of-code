from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.create_paddle()
    def create_paddle(self):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.setposition(self.x,self.y)

    def moveup(self):
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def movedown(self):
            y = self.ycor() - 20
            self.goto(self.xcor(), y)