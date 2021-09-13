"""
exercise
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Fsk_menu.json&name=Step%2010&url=worlds%2Fsk%2Fstep10.json

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
    move()
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
    
for step in range(6):
    jump()
