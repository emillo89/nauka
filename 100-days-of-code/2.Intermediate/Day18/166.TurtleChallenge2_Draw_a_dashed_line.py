from turtle import Turtle, Screen

timmy = Turtle()

"""
Pull the pen down - drawing when moving
Pull the pen up - no drawing when moving
"""


for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



screen = Screen()
screen.exitonclick()