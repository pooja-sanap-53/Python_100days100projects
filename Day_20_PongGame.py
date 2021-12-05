# Day 20
# Date: 04 Dec 2021
# The Pong Game 

from turtle import Turtle, Screen 
import time 


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # move paddle up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # move paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # to bounce back the ball after colliding with wall
    def bounce_y(self):
        self.y_move *= -1
        
    # to bounce ball back after colliding with paddle 
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # to reset position 
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        
    def r_point(self):
        self.r_score += 1


screen = Screen()
screen.setup(width =800, height=600)
screen.bgcolor("black")
screen.title("THE PONG GAME")
screen.tracer(0)

# Initializing paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Initializing ball
ball = Ball()

# Initializing score 
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collison with top and bottom wall
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()
        print("collided with wall")

    # detect collision with right and left paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>340) or  (ball.distance(l_paddle)<50 and ball.xcor()<-340):
        ball.bounce_x()
        

    # Detect when right paddle misses the ball
    if ball.xcor()>380:
        ball.reset()
        score.l_point()
        score.update_scores()

    # Detect when left paddle misses the ball
    if ball.xcor()<-380:
        ball.reset()
        score.r_point()
        score.update_scores()

    

screen.exitonclick()
