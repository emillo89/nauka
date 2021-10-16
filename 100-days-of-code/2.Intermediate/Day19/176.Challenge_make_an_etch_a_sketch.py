from turtle import Turtle, Screen

tim = Turtle()


def forward():
    """Draw forward"""
    tim.forward(10)


def backwards():
    """Draw backward"""
    tim.backward(10)


def turn_left():
    """Turn your turtle about 10 angle on your left"""
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    """Turn your turtle about 10 angle on your right"""
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_turtle():
    """clear all the drawing screen and take our turtle back to the beginning. """
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key = 'w', fun = forward)
screen.onkey(key = 's', fun = backwards)
screen.onkey(key = 'a', fun = turn_left)
screen.onkey(key = 'd', fun = turn_right)
screen.onkey(key = 'c', fun = clear_turtle)

screen.exitonclick()