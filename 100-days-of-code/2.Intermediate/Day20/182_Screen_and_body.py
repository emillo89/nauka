from turtle import Turtle, Screen

snake = []
for square in range(3):
    new_brick = Turtle("square")
    new_brick.color("white")
    new_brick.penup()
    snake.append(new_brick)

snake[0].goto(x=200, y=0)
snake[1].goto(x=snake[0].xcor() - 20, y=snake[0].ycor())
snake[2].goto(x=snake[1].xcor() - 20, y=snake[1].ycor())

# set width, height, bgcolor
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake by Emil")
screen.exitonclick()
