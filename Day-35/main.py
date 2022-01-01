import requests
from requests import api
from twilio.rest import Client

api_key = '5653befe016280e1d6c6fe4df872a962'
account_sid = 'AC12714f86fe9477e88e7510d15e667f0a'
auth_token = '585b76dc0643ea821d3ba0819234ec62'

city_name = 'Anand,India'

w_params = {
    'lat':10.2900,
    'lon':79.3500,
    'appid':api_key,
    'exclude':'current,minutely,daily'
}

the_link = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url=the_link, params=w_params)

response.status_code

the_data = response.json()

will_rain = False

for i in range(13):
    the_id = (the_data['hourly'][i]['weather'][0]['id'])
    if the_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's gonna rain! Bring your umbrella!",
        from_='+17345303819',
        to='+917698564711'
    )
    print(message.status)