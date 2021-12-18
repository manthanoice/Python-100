from turtle import *

ALIGNMENT = 'center'
FONT = ('Couries', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('E:\Python 100\Day-24\score.txt') as file:
            self.num = (int(file.read()))
        self.penup()
        self.score = 0
        self.highscore = self.num
        self.color('white')
        self.goto(-10, 280)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write("Your Score: {}    High Score: {}".format(self.score, self.highscore), align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('E:\Python 100\Day-24\score.txt', mode='w') as file:
                self.num = self.highscore
                file.write(str(self.num))
        self.score = 0
        self.update_scoreboard()
    
    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)