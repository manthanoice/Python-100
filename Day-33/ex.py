import requests


kanye = requests.get(url='https://api.kanye.rest/')
kanye_quote = kanye.json()
print(kanye_quote['quote'])