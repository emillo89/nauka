import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -90, -30, 30, 90, 150]
all_turtle = []

for position in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[position])
    new_turtle.color(colors[position])
    all_turtle.append(new_turtle)

print(all_turtle)


def finish():
    """Border where the turtles have a finish place"""
    meta = Turtle()
    meta.shape("square")
    meta.penup()
    meta.setposition(230, 0)
    meta.turtlesize(stretch_wid=18, stretch_len=0.2)


if user_bet:
    is_race_on = True

finish()

while is_race_on:
    for turtle in all_turtle:
        step = random.randint(0, 10)
        turtle.forward(step)
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            "#pencolor not color because color return set ('pencolor','fillcolor')"
            winner_turtle_color = turtle.pencolor()
            if winner_turtle_color == user_bet:
                print(f"You've won. Whe {winner_turtle_color} turtle is the winner")
            else:
                print(f"You've lose. Whe {winner_turtle_color} turtle is the winner")

screen.exitonclick()
