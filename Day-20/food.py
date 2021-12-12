from turtle import *
import random

class Food(Turtle):

    def __init__(self):
        '''
        To create food
        '''
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        '''
        To change location of food on the screen
        '''
        num_x = random.randint(-280, 280)
        num_y = random.randint(-280, 280)
        self.goto(num_x, num_y)