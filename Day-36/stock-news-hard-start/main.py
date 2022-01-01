import requests
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

the_params = {
    'function':'TIME_SERIES_INTRADAY',
    'symbol':STOCK,
    'interval':'60min',
    'apikey':'YKNMMVKPKRDP5VGH'
}

the_request = requests.get(STOCK_ENDPOINT, params=the_params)

the_request.status_code

the_data = the_request.json()

today = float(the_data['Time Series (60min)']['2021-12-31 12:00:00']['4. close'])
yesterday = float(the_data['Time Series (60min)']['2021-12-30 12:00:00']['4. close'])

print('Today is: {}'.format(today))
print('Yesterday is: {}'.format(yesterday))

diff = abs(yesterday - today)

the_perc = round((diff/ yesterday) * 100, 2)

print(the_perc)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_api = 'c11b2b15d0384ed3b8a3e1f0ca3a580a'
news_params = {
    'q':COMPANY_NAME,
    'apiKey':news_api
}
if the_perc > 1:

    the_news = requests.get(NEWS_ENDPOINT,params=news_params)

    the_news.raise_for_status

    articles = the_news.json()['articles']

    three_articles = articles[:3]
    for i in range(3):
        print('\n')
        the_title = three_articles[i]['title']
        the_desc = three_articles[i]['description']
        print(the_title)    



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""