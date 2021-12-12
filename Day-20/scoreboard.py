from turtle import *

ALIGNMENT = 'center'
FONT = ('Couries', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        '''
        To show the score
        '''
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(-10, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        '''
        To update the scoreboard
        '''
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT)
    
    def increase_scoreboard(self):
        '''
        To increase the user's score on the screen
        '''
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        '''
        To display Game is over one the center of the screen
        '''
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)