from turtle import Turtle,Screen
tim = Turtle()
for _ in range (15):
    tim.forward(15)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(15)
screen = Screen()
screen.exitonclick()