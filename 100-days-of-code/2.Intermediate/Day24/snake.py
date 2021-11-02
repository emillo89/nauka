from turtle import Turtle

STARTTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        """Create a object with color, shape and position on the screen"""
        for position in STARTTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        """Add a new segment to the snake"""
        new_brick = Turtle("square")
        new_brick.goto(position)
        new_brick.color("white")
        new_brick.penup()
        self.snake_segments.append(new_brick)

    def reset(self):
        """Reseting a snake"""
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head =self.snake_segments[0]

    def extend(self):
        """Add a new segment to the snake to the same position as the last segment."""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        """How can snake walk."""
        # for example range(start, stop, step)
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """If current heading is pointed down, it can't move up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """If current heading is pointed UP, it can't move down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """If current heading is pointed left, it can't move right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """If current heading is pointed down, it can't move right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
