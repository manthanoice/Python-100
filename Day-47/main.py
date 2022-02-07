from bs4 import BeautifulSoup
import requests
import smtplib
from mailpass import *

#Getting receiver's mail
receiver_mail = input('Enter your mail: ')

#Getting product url
url = input('Enter the URL of product you want to track: ')

#header for the request
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


#defining sender's mail and password
sender_mail = mail
sender_password = password

#getting content
content = requests.get(url=url, headers=header)

#getting text from the content <- Athough this can be done in one line above but we move lmao :P
the_content = content.text

#let's make the soup beachesss
soup = BeautifulSoup(the_content, 'html.parser')

#finding the product's name/title
the_name = soup.find('span', id='productTitle').getText().strip()

#finding the product's price
the_price = int(soup.find('span', class_='a-price-whole').getText().replace(',','').strip('.'))

#getting the minimum price from the user
user_price = int(input('Enter what should be the minimum price of product when we should send you alerts: '))

#sending mail using smtp
if the_price <= user_price:
    #the message which we will mail to user
    message = 'The price of {} is now only {}'.format(the_name, the_price)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(sender_mail, password=sender_password)
        connection.sendmail(
            from_addr=sender_mail,
            to_addrs=receiver_mail,
            msg='Subject: Amazon Price Alert \n\n{}\n{}'.format(message, url)
        )