from turtle import *

class Ball(Turtle):
    def __init__(self):
        '''
        To create the ball
        '''
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        '''
        To move the ball
        '''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        '''
        To make the ball bounce vertically
        '''
        self.y_move *= -1
    
    def bounce_x(self):
        '''
        To make the ball bounce horizontally
        '''
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()