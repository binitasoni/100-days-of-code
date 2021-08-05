from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
    def move_ball(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.setposition(x,y)
    def bounce_y(self):
        self.y=self.y*-1

    def bounce_x(self):
        self.x= self.x * -1
    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()