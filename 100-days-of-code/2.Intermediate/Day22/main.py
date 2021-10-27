from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((300,0))
l_paddle = Paddle((-300,0))

screen.listen()

#Controlled right paddle
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

#Controlled left paddle
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()