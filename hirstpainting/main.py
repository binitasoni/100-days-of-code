# import colorgram
# rgb=[]
# d=colorgram.extract("image.jpg", 30)
# for colors in d:
#   r=colors.rgb.r
#   b=colors.rgb.b
#   g=colors.rgb.g
#   a=(r,g,b)
#   rgb.append(a)
#
# print(rgb)
color=[ (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
import turtle,random
turtle.colormode(255)
tim=turtle.Turtle()
def func():
 for i in range(10):
  tim.pendown()
  tim.begin_fill()
  tim.circle(10)
  tim.end_fill()
  tim.color(random.choice(color))
  tim.forward(50)
  tim.speed(100)
j=0
a=0
for i in range(10):

  tim.setposition(i,j)
  a=a+50
  j=j+50
  func()
screen=turtle.Screen()
screen.exitonclick()
