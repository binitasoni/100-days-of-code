import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
t=[]
def create_block():
    chance=random.randint(1,6)
    if chance==1:
      a=CarManager()
      t.append(a)

player_turtle=Player()
screen.listen()
screen.onkey(player_turtle.move, key="Up")
score=Scoreboard()
text=Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    create_block()
    for turtle in t:
        turtle.move_ahead()
    for turtle in t:
        if turtle.distance(player_turtle)<50:

            game_is_on=False
    if player_turtle.ycor()>260:
        score.update()
        for turtle in t:
            turtle.increase_speed()
        player_turtle.goto(0, -280)
text.game_over()


