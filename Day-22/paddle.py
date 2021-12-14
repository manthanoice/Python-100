from turtle import *

class Paddle(Turtle):
    def __init__(self, where):
        super().__init__()
        '''
        To create the paddle

        Arguments: Location of paddle as a tuple
        Ex: (200, 200)
        '''
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(where)
    
    def go_up(self):
        '''
        To move the paddle upwards
        '''
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)
    
    def go_down(self):
        '''
        To move the paddle downwards
        '''
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)