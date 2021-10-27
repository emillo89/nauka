from turtle import Screen, Turtle
import padle
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

padle = Turtle('square')
padle.penup()
padle.shapesize(stretch_wid=5, stretch_len=1)
padle.goto(x=350, y=0)
padle.color('white')

def go_up():
    new_y = padle.ycor() + 20
    padle.goto(padle.xcor(), new_y)

def go_down():
    new_y = padle.ycor() - 20
    padle.goto(padle.xcor(), new_y)


screen.listen()
screen.onkey(fun=go_up, key='Up')
screen.onkey(fun=go_down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()