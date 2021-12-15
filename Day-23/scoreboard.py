from turtle import *

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-80, 260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write("Level: {}".format(self.level),font=FONT, align="left")

    def level_increase(self):
        self.level +=1
        self.update_score()
    