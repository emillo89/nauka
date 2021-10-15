import random
from turtle import Turtle, Screen


tim = Turtle()

"""Random colors draw"""
colors = ["dark blue","gray","khaki","tan","sienna","magenta","deep pink","red","gold","spring green","azure",
          "silver","yellow","medium violet red","orange red","black"]

"""Random direction walk """
angle = [0,90,180,270]
tim.pensize(15)

"""Create one direction step"""
def move():
    """Create a random angle, color and speed for one draw-step"""
    what_angle = random.choice(angle)
    what_color = random.choice(colors)
    what_speed = random.randint(1,11)

    tim.speed(what_speed)
    tim.color(what_color)
    tim.forward(100)
    tim.setheading(what_angle)


for _ in range(50):
    move()

screen = Screen()
screen.exitonclick()