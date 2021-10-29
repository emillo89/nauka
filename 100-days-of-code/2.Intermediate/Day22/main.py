from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((330, 0))
l_paddle = Paddle((-330, 0))

ball = Ball()
screen.listen()

'#Controlled right paddle'
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

'#Controlled left paddle'
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    '# Detect collision with r_paddle'
    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) < 50 and ball.xcor() < -300:
        ball.bounce_x()
        # print('Made contact')
screen.exitonclick()

