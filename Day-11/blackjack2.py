import random
from replit import clear

def card_picker():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_sums(user_sum, computer_sum):
    if user_sum == 0:
        return "You got blackjack! You won! WooHoo! 💃🕺"
    elif computer_sum == 0:
        return "Computer got blackjack! You lost F! 😿"
    elif user_sum == computer_sum:
        return "It's a draw! You faugh well soldier! 🤝"
    elif user_sum > 21:
        return "You lost cause you went over! What's wrong with you pal? 😔"
    elif computer_sum > 21:
        return "Opponenet went over! You won! Woohoo 💃🕺"
    elif user_sum > 21 and computer_sum > 21:
        return "You went over! You lost 😔"
    elif user_sum > computer_sum:
        return "You won! WooHoo! 💃🕺"
    else:
        return "You lost! F for fallen soldier!"

def the_game():
    print("""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
            |  \/ K|                            _/ |                
            `------'                           |__/           """)
    game_over = False
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(card_picker())
        computer_cards.append(card_picker())
    while not game_over:
        user_sum = calc_score(user_cards)
        computer_sum = calc_score(computer_cards)
        print("Your cards are {}, current score: {}".format(user_cards, user_sum))
        print("Computer's first card is {}".format(computer_cards[0]))
        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            game_over = True
        else:
            do_you_continue = input("Type 'y' if you want to add another card, else type 'n': ").lower()
            if do_you_continue == 'y':
                user_cards.append(card_picker())
            else:
                game_over = True
    while computer_sum !=0 and computer_sum < 17:
        computer_cards.append(card_picker())
        computer_sum = calc_score(computer_cards)
    print("Your final cards are {}, Final score: {}".format(user_cards, user_sum))
    print("Opponent's final cards are {}, Final score: {}".format(computer_cards, computer_sum))
    print(compare_sums(user_sum=user_sum, computer_sum=computer_sum))

while(input("Do you want to play black jack? 'y' or 'n': ")).lower() == 'y':
    clear()
    the_game()