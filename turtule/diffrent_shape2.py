from turtle import Turtle
tom = Turtle()

colors = ["red", "blue", "green", "navy", "gold", "violet","purple","black"]

def draw_shape(num_shides):
    angle = 360/num_shides
    for _ in range (num_shides):
        tom.forward(100)
        tom.right(angle)
        tom.color(colors[num_shides - 3])

for i in range(3, 11):
    draw_shape(i)
