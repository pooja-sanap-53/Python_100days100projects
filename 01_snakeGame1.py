# Create a snake body

from turtle import Turtle, Screen

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")

segment_1 = Turtle("square")
segment_1.color("white")
segment_1.goto(x=0, y =0)

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(x=-20,y=0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(x=-40,y=0)













screen.exitonclick()
