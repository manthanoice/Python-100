import requests

the_request = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
the_request.raise_for_status()

the_data = the_request.json()

question_data = the_data['results']