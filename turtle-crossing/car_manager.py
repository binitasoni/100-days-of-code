COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
def num():
    return random.randint(-300,300)
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(random.randint(250,300),num())
        self.forward(STARTING_MOVE_DISTANCE)
        self.car_speed=STARTING_MOVE_DISTANCE

    def move_ahead(self):
        x=self.xcor()-3*self.car_speed
        y=self.ycor()
        self.goto(x,y)
    def increase_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE+MOVE_INCREMENT
