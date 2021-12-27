import requests
from datetime import datetime

the_params = {
    'lat' : 22.2587,
    'lng' : 71.1924,
    'formatted': 0
}

the_request = requests.get(url='https://api.sunrise-sunset.org/json', params=the_params)
the_request.raise_for_status()
data = the_request.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)