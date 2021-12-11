from turtle import *
import random

screen = Screen()
screen.setup(height=400, width=500)

is_race_on = False
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle do you think will win the race? Enter your color: ")
print(user_bet)

colors = ['red', 'green', 'pink', 'orange', 'purple', 'blue']

positions = [-70, -40, -10, 20, 50, 80]

totos = []

for i in range(0, 6):
    new_toto = Turtle(shape='turtle')
    new_toto.penup()
    new_toto.color(colors[i])
    new_toto.setpos(x=-230, y=positions[i])
    totos.append(new_toto)

if user_bet:
    is_race_on = True

while is_race_on:
    for the_toto in totos:
        if the_toto.xcor() > 230:
            is_race_on = False
            winner_color = the_toto.pencolor()
            if winner_color == user_bet:
                print("You've won the bet! The {} turtle is the winner!".format(winner_color))
            else:
                print("Oops! You lost the race! The winner is {} turtle!".format(winner_color))
        num = random.randint(1, 10)
        the_toto.forward(num)


screen.exitonclick()