print("Welcome to the tip calculator!")
bill = float(input("What is your total bill: "))
tip = int(input("How much % tip you want to give: "))
people = int(input("How many people are there: "))
answer = round((bill/people)*((tip/100)+1),2)
print("Per person tip should be {} rupees".format(answer))