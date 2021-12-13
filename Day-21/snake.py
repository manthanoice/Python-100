from turtle import *

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    

    
    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)
    
    def add_segment(self, position):
        toto = Turtle(shape='square')
        toto.penup()
        toto.color('white')
        toto.goto(position)
        self.segments.append(toto)
        
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num-1].xcor()
            new_y = self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)