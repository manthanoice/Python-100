from turtle import *

ALIGNMENT = 'center'
FONT = ('Couries', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(-10, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT)
    
    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)