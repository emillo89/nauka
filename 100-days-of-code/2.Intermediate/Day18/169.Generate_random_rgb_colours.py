import random
# from turtle import Turtle, Screen
import turtle as t



tim = t.Turtle()
# change the color mode, then create a random color
t.colormode(255)

# Random direction walk
angle = [0,90,180,270]
tim.pensize(15)

def random_color():
    """Create a random color for your step"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup



def move():
    """Create a random angle and speed for one draw-step"""
    what_angle = random.choice(angle)
    what_speed = random.randint(1,11)
    what_color = random_color()


    tim.speed(what_speed)
    tim.pencolor(what_color)
    tim.forward(100)
    tim.setheading(what_angle)


for _ in range(50):
    move()
