import random
from replit import clear

logo = '''
 /$$   /$$                                                    /$$$$$$                                         /$$                    
| $$$ | $$                                                   /$$__  $$                                       |__/                    
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$       | $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ 
| $$ $$ $$| $$  | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$      | $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/| $$| $$__  $$ /$$__  $$
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/      | $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$_____/| $$            | $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$| $$  | $$| $$  | $$
| $$ \  $$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/| $$| $$  | $$|  $$$$$$$
|__/  \__/ \______/ |__/ |__/ |__/ \_______/|__/             \______/  \______/  \_______/|_______/|_______/ |__/|__/  |__/ \____  $$
                                                                                                                            /$$  \ $$
                                                                                                                           |  $$$$$$/
                                                                                                                            \______/ 
'''

def num_gen():
    return random.randint(1, 100)

def difficulty():
    the_difficulty = input("Enter the difficulty level 'easy' or 'hard': ")
    if the_difficulty == 'easy':
        return 10
    else:
        return 5

def checking_answer(generated_number, guessed_number, turns):
    if guessed_number > generated_number:
        print("Your guess is too high")
        return turns - 1
    elif guessed_number < generated_number:
        print("Your guess is too low")
        return turns - 1
    else:
        print("You guessed it! Correct number was {}".format(generated_number))

def game():
    print(logo)
    print("Welcome to guessing the number game: ")
    print("I am thinking of number between 1 and 100!")
    generated_number = num_gen()
    print("Correct answer is {}".format(generated_number)) #Debugging purpose!
    the_difficulty = difficulty()
    guess = 0
    while guess != generated_number:
        print("You have {} chances to guess".format(the_difficulty))
        guess = int(input("Enter your guess: "))
        the_difficulty = checking_answer(generated_number, guess, the_difficulty)
        if the_difficulty == 0:
            print("You lose")
            return
        elif guess != generated_number:
            print("Guess again!")

while input("Are you ready to play number guessing game? 'y' or 'n': ").lower() == 'y':
    clear()
    game()