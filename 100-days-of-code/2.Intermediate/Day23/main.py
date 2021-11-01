import time
from turtle import Screen
from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.move, key='Up')


game_is_on = True
while game_is_on:
    for i in range(10):
        car = CarManager()
        time.sleep(0.1)
        screen.update()


screen.exitonclick()