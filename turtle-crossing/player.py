"""Player module"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Player"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """go up"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """go to start"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """is at finish line"""
        return self.ycor() > FINISH_LINE_Y
