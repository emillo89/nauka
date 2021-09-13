"""
exercise
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
"""


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def left_up():
    turn_left()
    move()


def right_down():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def jump():
    left_up()
    right_down()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


