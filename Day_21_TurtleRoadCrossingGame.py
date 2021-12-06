# Day 21
# Date: 05 Dec 2021
# Turtle Road Crossing Game

from turtle import Turtle, Screen
import random
import time 

COLORS = ["red", "orange", "yellow", "green", "cyan", "chocolate"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
FONT = ("Courier", 15, "normal")


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    # moving player 
    def move_player(self):
        self.forward(MOVE_INCREMENT)
        
    # going to start position
    def go_to_start(self):
        self.goto(STARTING_POSITION)


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed= STARTING_MOVE_DISTANCE
      
        
    # creating cars 
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car= Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid =1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_x = random.randint(280, 300)
            random_y = random.randint(-280, 280)
            new_car.goto(random_x, random_y)
            self.all_cars.append(new_car)

    # moving cars 
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed) 

    # level up speed
    def level_up(self):
        self.car_speed += STARTING_MOVE_DISTANCE


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)

    # increasing levels
    def increase_level(self):
        self.level += 1

    #updating score    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level :{self.level}", align="left", font=FONT)

    # game over 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
        

screen = Screen()
screen.setup(width =600, height = 600)
screen.title("TURTLE ROAD CROSSING GAME")
screen.bgcolor("white")
screen.tracer(0)

# Initializing player
player = Player()

# Initializing cars 
cars = CarManager()

# Initializing scoreboard
score = ScoreBoard()


screen.listen()
screen.onkey(player.move_player, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    
    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_on = False
            score.game_over()

    # reached other edge
    if player.ycor() > 280:
        player.go_to_start()
        cars.level_up()
        score.increase_level()
        score.update_scoreboard()
        


screen.exitonclick()  