import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url='https://api.sheety.co/8cd035ce8e01d3ce4df2b6f8ff6b0ea4/flightApi/sheet1')
        self.data = self.response.json()['sheet1']
    
    def get_city_code(self, city):
        self.city_code = self.data[city]['iataCode']
        print(self.city_code)