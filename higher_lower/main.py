from art import logo
from art import vs
from game_data import data
from replit import clear
import random
print(logo)
def select():
  d=list(data)
  a=random.choice(d)
  return a
def correct(A,B):
  if A['follower_count']>B['follower_count']:
    win="A"
  else:
    win="B"
  return win
option=1
score=0
A=select()
B=select()
while(option==1):
  print(f"option A:\n{A['name']},{A['description']},{A['country']}")
  print(vs)
  print(f"option B:\n{B['name']},{B['description']},{B['country']}")
  choice=input("Enter A or B: ")
  clear()
  if choice==correct(A,B):
   score=score+1
   print(f"correct choice,your score is {score}")
   if correct(A,B)=="B":
       A=B
       B=select()
   else:
     B=select()
  else: 
    print(f"Incorrect choice game ends,your score is {score}!")
    option=0
