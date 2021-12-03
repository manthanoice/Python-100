import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def card_choose():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_cards(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over! You lost 😔"
    if user_score == computer_score:
        return "It's a draw 👀!"
    elif computer_score == 0:
        return "Computer has blackjack! You lose 😔"
    elif user_score == 0:
        return "You have blackjack! You won! 💃"
    elif user_score > 21:
        return "You went over more than 21! You lose ☹️"
    elif computer_score > 21:
        return "Opponenet went over! You won! 🕺"
    elif user_score > computer_score:
        return "You win 😭"
    else:
        return "You lost! '😿"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(card_choose())
        computer_cards.append(card_choose())
    while not is_game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print("Your cards are: {} and current score: {}".format(user_cards, user_score))
        print("Computer's first card is: {}".format(computer_cards[0]))
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            do_you_want_to_continue = input("Enter 'y' if you want to get anoter card, 'n' to pass: ").lower()
            if do_you_want_to_continue == 'y':
                user_cards.append(card_choose())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_choose())
        computer_score = calc_score(computer_cards)
    print("Your final hand: {}, final score: {}".format(user_cards, user_score))
    print("Computer final hand: {}, final score: {}".format(computer_cards, computer_score))
    print(compare_cards(user_score=user_score, computer_score=computer_score))

while input("Do you want to play a game of blackjack? If yes type 'y' or type 'n': ").lower() == 'y':
    clear()
    play_game()