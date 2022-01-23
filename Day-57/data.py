import requests
import json

response = requests.get(url='https://api.npoint.io/e4b5fedd96faddb691d0').text

the_text = json.loads(response)

print('The titles: \n')
for i in range(3):
    print(the_text[i]['title'])

print('\nThe subtitles: \n')
for i in range(3):
    print(the_text[i]['subtitle'])

print('\nThe Body: \n')
for i in range(3):
    print(the_text[i]['body'])
    print('\n')