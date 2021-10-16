import random

import turtle as t

# It's copy a list rgb_colors without white colors (white colors we can deleted)
color_list = [(246, 243, 237), (224, 234, 242), (243, 225, 74), (179, 78, 29), (49, 36, 26),
              (219, 151, 76), (146, 28, 41), (22, 25, 69), (44, 43, 120), (243, 236, 239),
              (170, 21, 16), (48, 87, 158), (210, 85, 128), (156, 50, 86), (120, 160, 224),
              (27, 43, 28), (215, 79, 62), (139, 183, 140), (115, 106, 202), (75, 120, 57),
              (65, 30, 35), (157, 179, 231), (150, 211, 191), (204, 135, 43), (86, 87, 33),
              (87, 155, 109), (202, 121, 162), (61, 148, 170), (55, 100, 18)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# The place where we can start
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

nums_of_dots = 100


def random_colors():
    color = random.choice(color_list)
    return color


def hirst_painting():
    global nums_of_dots
    for _ in range(1, nums_of_dots + 1):
        tim.dot(20, random_colors())
        tim.forward(50)

        '#set next row (2 to 10)'
        if _ % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


hirst_painting()

screen = t.Screen()
screen.exitonclick()
