from turtle import Turtle,Screen 
tim = Turtle()
for _ in range (3):
    tim.color("red")
    tim.forward(100)
    tim.right(120)

for _ in range (4):
    tim.color("blue")
    tim.forward(100)
    tim.right(90)

for _ in range (5):
    tim.color("green")
    tim.forward(100)
    tim.right(72)

for _ in range (6):
    tim.color("violet")
    tim.forward(100)
    tim.right(60)

for _ in range (7):
    tim.color("orange")
    tim.forward(100)
    tim.right(51.42)

for _ in range(8):
    tim.color("purple")
    tim.forward(100)
    tim.right(45)

for _ in range(9):
    tim.color("navy")
    tim.forward(100)
    tim.right(40)

for i in range(10):
    tim.color("black")
    tim.forward(100)
    tim.right(36)

screen = Screen()
screen.exitonclick()
