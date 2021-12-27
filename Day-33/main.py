import requests

the_request = requests.get(url='http://api.open-notify.org/iss-now.json')
the_request.raise_for_status()

data = the_request.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)