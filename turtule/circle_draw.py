import turtle as t
import random 
tom = t.Turtle()
t.colormode(255)
tom.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_circle(5)

screen= t.Screen()
screen.exitonclick()

