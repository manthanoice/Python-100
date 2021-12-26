import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open('Day-32\quotes.txt', encoding='utf8') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    #add