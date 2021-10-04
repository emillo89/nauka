'''https://cs111.wellesley.edu/labs/lab01/colors'''

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink")
timmy.forward(220)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()




class Car():
    """atributes"""
    speed = 0
    fuel = 32

    """method1"""
    def move(self):
        self.speed = 60


    """method2"""
    def stop(self):
        self.speed = 0

volvo = Car()
print(volvo.speed)
volvo.move()
print(volvo.speed)
volvo.stop()
print(volvo.speed)