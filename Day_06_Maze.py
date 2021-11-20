# Day 06
# Date: 20 Nov 2021
# Maze Escape

'''
This was a challenge on website named : reeborg.ca
A json file is attached so that you can directly switch to the Maze World !

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
  
while at_goal() is False:
    if front_is_clear() is True:
        move()
    if front_is_clear() is False and wall_on_right() is True and wall_in_front is False:
        jump()
    if wall_on_right() is True and wall_in_front() is True:
        turn_left()
    if wall_on_right() is True and front_is_clear() is True:
        move()
    if front_is_clear() is True and wall_on_right() is False:
        turn_right()
    if front_is_clear() is False and wall_on_right() is False:
        turn_right()
    if wall_on_right() is True and wall_in_front() is True:
        turn_left()