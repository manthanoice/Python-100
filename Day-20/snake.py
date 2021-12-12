from turtle import *

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        '''
        To create the snake
        '''
        self.segmantes = []
        self.create_snake()
        self.head = self.segmantes[0]

    def create_snake(self):
        '''
        To create the snake
        '''
        for position in starting_position:
            self.add_segment(position)
            
    def add_segment(self, position):
        '''
        Too add one segment to the snake
        '''
        toto = Turtle(shape='square')
        toto.penup()
        toto.color('white')
        toto.goto(position)
        self.segmantes.append(toto)
    
    def extend_segment(self):
        '''
        To extend the snake
        '''
        self.add_segment(self.segmantes[-1].position())
    
    def move(self):
        '''
        To move the snake in forward direction
        '''
        for segmante_num in range(len(self.segmantes)-1, 0, -1):
            new_x = self.segmantes[segmante_num - 1].xcor()
            new_y = self.segmantes[segmante_num - 1].ycor()
            self.segmantes[segmante_num].goto(new_x, new_y)
        self.segmantes[0].forward(move_distance)
    
    def up(self):
        '''
        To move snake upwards
        '''
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        '''
        To move snake downwards
        '''
        if self.head.heading()!= UP:
            self.head.setheading(270)
    
    def left(self):
        '''
        To move snake left
        '''
        if self.head.heading()!= RIGHT:
            self.head.setheading(180)
    
    def right(self):
        '''
        To move snake right
        '''
        if self.head.heading()!= LEFT:
            self.head.setheading(0)