from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# set width, height, bgcolor
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake by Emil")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detective collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detective collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_in_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_in_on = False
            score.game_over()
screen.exitonclick()
