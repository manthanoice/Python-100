from game_data import the_data
import random
from art import the_logo
from art import vs
import os

def game():
    score = 0
    num_1 = random.randint(0, 49)
    choice_a = the_data[num_1]
    should_continue = True
    while should_continue:
        print(the_logo)
        print("Your score is {}".format(score))
        num_2 = random.randint(0, 49)
        if num_1 == num_2:
            num_2 = random.randint(0, 49)
        choice_b = the_data[num_2]
        print("Compare A: {}, a {}, from {}!".format(choice_a['name'], choice_a['description'], choice_a['country']))
        print(vs)
        print("Against B: {}, a {}, from {}!".format(choice_b['name'], choice_b['description'], choice_b['country']))
        your_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if your_guess == 'A' and choice_a['follower_count'] > choice_b['follower_count']:
            score+=1
            choice_b = choice_a
            os.system('cls')
        elif your_guess == 'B' and choice_b['follower_count'] > choice_a['follower_count']:
            score+=1
            choice_b = choice_a
            os.system('cls')
        else:
            print("Oops Wrong answer! You lost! :( and your final Score is {}".format(score))
            should_continue = False

while input("Do you want to play the game? 'Y' or 'N': ").lower() == 'y':
    game()