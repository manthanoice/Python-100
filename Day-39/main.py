# #This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from data_manager import *

# data_manager = DataManager()

# data_manager.get_city_code('Paris')

import requests

response = requests.get(url='https://api.sheety.co/8cd035ce8e01d3ce4df2b6f8ff6b0ea4/flightApi/sheet1')
data = response.json()['sheet1']
print(data)