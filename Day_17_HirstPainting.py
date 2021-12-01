# Day 17
# Date: 01 Dec 2021
# Hirst Painting

import turtle as t 
import random 
# import colorgram

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    color = (r,g,b)
    return color

tim.shape("arrow")
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)

for i in range(1,101):
    tim.color(random_color())
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
screen = t.Screen()
screen.exitonclick()