import random
from turtle import Turtle, Screen

tim = Turtle()



"""Draw a shape"""
def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)


colors = ["dark blue","gray","khaki","tan","sienna","magenta","deep pink"]

for shape_side_n in range(3, 11):

    draw_shape(shape_side_n)
    color = random.choice(colors)
    tim.color(color)


screen = Screen()
screen.exitonclick()