# Day 19
# Date: 03 Dec 2021
# Snake Game

from turtle import Turtle, Screen
import time 
import random

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head= self.segments[0]

# Creating snake
    def create_snakes(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

# Moving snake
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

# Controls 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# Add the segment
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


# Extending the tail 
    def extend(self):
        self.add_segment(self.segments[-1].position())
          


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid = 0.5)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

# reloads food
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score = {self.score}", align= ALIGNMENT, font= FONT)

# increases score 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER !", align=ALIGNMENT, font = FONT)
        

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # collision with food 
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # collision with wall
    if snake.head.xcor()>298 or snake.head.xcor()< -298 or snake.head.ycor()>298 or snake.head.ycor()<-298:
        is_on= False
        scoreboard.game_over()

    # collision with tail 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif segment != snake.head:
            if snake.head.distance(segment)<10:
                is_on = False
                scoreboard.game_over()

screen.exitonclick()