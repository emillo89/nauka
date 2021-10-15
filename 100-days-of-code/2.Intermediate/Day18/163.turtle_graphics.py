from turtle import Turtle, Screen

"""create a Turtle"""
timmy_the_turtle = Turtle()

"""set turtle shape"""
timmy_the_turtle.shape("turtle")

"""set turtle color"""
timmy_the_turtle.color("purple")

"""Move the turtle forward by the specified distance"""
timmy_the_turtle.forward(100)

"""Turn turtle right by angle units"""
timmy_the_turtle.right(120)

"""create a screen"""
screen = Screen()
screen.exitonclick()