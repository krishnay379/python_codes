import turtle as t
import random
tom = t.Turtle()
t.colormode(255)
color_list =[(202, 164, 109), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (168, 99, 102), (177, 40, 51), (233, 175, 166), (8, 46, 55), (111, 94, 97), (193, 144, 159), (104, 17, 8), (174, 94, 97), (176, 192, 208), (54, 45, 50), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (168, 99, 102), (177, 40, 51), (233, 175, 166), (8, 46, 55), (111, 94, 97), (193, 144, 159)]

tom.penup()
tom.hideturtle()
tom.speed("fastest")
tom.setheading(200)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):

   tom.dot(20, random.choice(color_list))
   tom.forward(50)
   if dot_count %10 ==0:
         tom.setheading(90)
         tom.forward(50)
         tom.setheading(180)
         tom.forward(500)
         tom.setheading(0)

screen = t.Screen()
screen.exitonclick()
