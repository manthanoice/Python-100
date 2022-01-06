# #This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from data_manager import *

# data_manager = DataManager()

# data_manager.get_city_code('Paris')

from typing import final
import requests

response = requests.get(url='https://api.sheety.co/8cd035ce8e01d3ce4df2b6f8ff6b0ea4/flightApi/sheet1')
data = response.json()['sheet1']

response_2 = requests.get(url='https://tequila-api.kiwi.com/locations/query?term=PRG&locale=en-US&location_types=airport&limit=10&active_only=true')
print(response_2)

for i in range(len(data)):
    the_data = data[i]
    if the_data['city'] == 'Paris':
        print(the_data['iataCode'])