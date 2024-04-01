"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    move()
    jump()


def jump():
    """
    pre_condition:karel is on the left side of the wall, facing_east
    post_condition:karel is on the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    pre_condition:karel is on the left side of the wall, facing_east
    post_condition:karel is facing_north
    """
    turn_left()
    #Facing NORTH
    while not right_is_clear():
        move()


def cross():
    """
    pre_condition:karel is facing_north
    post_condition:karel is at the upper right, facing_south
    """
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()

def down():
    """
    pre_condition:karel is at the upper right, facing_south
    post_condition:karel is facing_south
    """
    while front_is_clear():
        move()


def main():
    """
    karel crossed hurdles in a 12*12 world with a far loop
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()










# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
