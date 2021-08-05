import turtle,pandas
screen=turtle.Screen()
tim=turtle.Turtle()
screen.title("Guess the state")
image="/Users/anupamsarfare/Desktop/india_map.gif"
screen.addshape(image)
tim.shape(image)
data=pandas.read_csv("india_states.csv")
states=data["state"].to_list()
x=data["x"].to_list()
y=data["y"].to_list()
option=1
guessed_state=0
answered=[]
missed=[]
while option:
 answer_state=screen.textinput(title=f"{guessed_state}/36 guessed correctly",prompt="Enter State name").title()
 answered.append(answer_state)
 if answer_state=="Exit":
     break
 for state in states:
    if(answer_state==state):
        guessed_state = guessed_state+1
        i=states.index(state)
        x_pos=x[i]
        y_pos=y[i]
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x_pos,y_pos)
        turtle.color('blue')
        turtle.write(state, move=False, align="left", font = ("Arial",9,"bold"))
for state in states:
    if state not in answered:
        missed.append(state)
df = pandas.DataFrame(missed, columns=["colummn"])
df.to_csv('list.csv', index=False)
print(df)
screen.exitonclick()