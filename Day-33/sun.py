import requests
from datetime import datetime
import time
import smtplib

the_params = {
    'lat' : 22.2587,
    'lng' : 71.1924,
    'formatted': 0
}

my_mail = 'fortheapiss@gmail.com'
my_password = 'lolyouthoughtiwouldputmypasswordhere?'

def is_night():
    the_request = requests.get(url='https://api.sunrise-sunset.org/json', params=the_params)
    the_request.raise_for_status()
    data = the_request.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return True

def is_is_visible():
    the_request = requests.get(url='http://api.open-notify.org/iss-now.json')
    the_request.raise_for_status()
    data = the_request.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    lat = the_params['lat'] - 5
    lng = the_params['lng'] - 5
    if lat <= iss_lat <= lat+10 and lng <= iss_lng <= lng+10:
        return True

while True:
    time.sleep(60)
    if is_is_visible() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_mail, my_password)
        connection.sendmail(
            from_addr = my_mail,
            to_addrs = 'sahiltotala972@gmail.com',
            msg ='Look up For ISS')