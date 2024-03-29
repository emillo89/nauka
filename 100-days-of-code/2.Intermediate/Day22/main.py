from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()

'#Controlled right paddle'
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

'#Controlled left paddle'
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

def game():
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed )
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        '# Detect collision with r_paddle and l_paddle'
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.move_speed



        '#Dectect when the ball goes out r_paddle'
        if ball.xcor() > 380 :
            ball.reset_position()
            scoreboard.l_point()

        '#Derect when the ball goes out l_paddle misses'
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()



game()



screen.exitonclick()

