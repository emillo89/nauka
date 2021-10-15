import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    """Create a random color for your step"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

tim.speed("fastest")

def draw_spirograph(size_of_the_gap):
    """Create a spirograph when you write a gap between for two cirle"""
    for _ in range(int(360 / size_of_the_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_the_gap)
        tim.circle(120)

draw_spirograph(1)


screen = t.Screen()
screen.exitonclick()