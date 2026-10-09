from turtle import Turtle,Screen
import random

screen= Screen()
screen.setup(width = 500,height =400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which title will win the race ?  Enter a color :")
color=["red","green","purple","blue","violet"]
y_positions =[-70,-40,-10,20,50,80]

ram = Turtle(shape = "turtle")
ram
ram.penup()
ram.goto(x=-230,y=y_positions[turtle_index])

shyam = Turtle(shape = "turtle")
shyam.penup()
shyam.goto(-230,y=y_positions[turtle_index])

hanuman = Turtle(shape ="turtle")
hanuman.penup()
hanuman.goto(-230,0)

narayan = Turtle(shape="turtle")
narayan.penup()
narayan.goto(-230,50)

lakshmi = Turtle(shape="turtle")
lakshmi.penup()
lakshmi.goto(-230,100)

ram.color("red")
shyam.color("blue")
hanuman.color("green")
narayan.color("violet")
lakshmi.color("gold")

def race():
    ram.forward(random.randint(1,10))
    shyam.forward(random.randint(1,10))
    hanuman.forward(random.randint(1,10))
    narayan.forward(random.randint(1,10))
    lakshmi.forward(random.randint(1,10))

screen.exitonclick()