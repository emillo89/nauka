from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)
        self.x_cor = 10
        self.y_cor = 10

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        """When the ball detected collision with wall and bounce in the Y direction."""
        self.y_cor *= -1

    def bounce_x(self):
        """when the ball detected collision with paddle and bounce in the X direction"""
        self.x_cor *= -1
