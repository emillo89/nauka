from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color('white')

    def go_up(self):
        """Paddle go up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Paddle go down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




