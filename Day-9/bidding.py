from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

is_bidding_finished = False

bids = {}

def highest(biddings):
    for bidder in biddings:
        highest_amount = 0
        amount = biddings[bidder]
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder
    print('The winner is {} and the highest bid is {}!'.format(winner, highest_amount))

while not is_bidding_finished:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bids[name] = bid
    others = input("Are there any other bidders? 'Yes' or 'No': ").lower()
    if others == 'no':
        is_bidding_finished = True
        highest(biddings=bids)
    elif others == 'yes':
        clear()