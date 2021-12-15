from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.go_back_to_starting_position()
        self.left(90)
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    def go_back_to_starting_position(self):
        self.goto(STARTING_POSITION)