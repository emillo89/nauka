from turtle import Turtle, Screen
import time
starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for position in starting_position:
    new_brick = Turtle("square")
    new_brick.goto(position)
    new_brick.color("white")
    new_brick.penup()
    snake_segments.append(new_brick)


# snake_segments[0].goto(x=00, y=0)
# snake_segments[1].goto(x=snake_segments[0].xcor() - 20, y=snake_segments[0].ycor())
# snake_segments[2].goto(x=snake_segments[1].xcor() - 20, y=snake_segments[1].ycor())

starting_position

# set width, height, bgcolor
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake by Emil")
screen.tracer(0)


game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)

    # for example range(start, stop, step)
    for seg_num in range(len(snake_segments) -1 , 0, -1):
        new_x = snake_segments[seg_num - 1].xcor()
        new_y = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(x=new_x, y=new_y)



screen.exitonclick()
