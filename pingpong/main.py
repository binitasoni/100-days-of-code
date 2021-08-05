from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.tracer(0)
screen.listen()
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
r_score=score()
l_score=score()
screen.onkey(fun=r_paddle.moveup,key="Up")
screen.onkey(fun=r_paddle.movedown,key="Down")
screen.onkey(fun=l_paddle.moveup,key="s")
screen.onkey(fun=l_paddle.movedown,key="w")



b=Ball()
option=1
while option:
  time.sleep(0.1)
  screen.update()
  b.move_ball()
  if b.ycor()>280 or b.ycor()<-280:
    b.bounce_y()
  if b.distance(r_paddle)<50 and b.xcor()>320:
    r_score.r__score()
    b.bounce_x()
  if b.distance(l_paddle) < 50 and b.xcor() < -320:
    l_score.l__score()
    b.bounce_y()
  if b.xcor()>380:
    b.reset_pos()
  if b.xcor()<-380:
    b.reset_pos()


screen.exitonclick()