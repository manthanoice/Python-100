import requests
from requests.api import head
from datetime import datetime

pixela_url = 'https://pixe.la/v1/users'

user = 'pebkac'
token = 'ubiudb93feuwbfeuib'

user_params = {
    'token':token,
    'username':user,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)

graph_params = {
    'id':'thegraph69420',
    'name':'Coding Graph',
    'unit':'Minutes',
    'type':'int',
    'color':'sora'
}

headers = {
    'X-USER-TOKEN': token
}

# graph_endpoint = '{}/{}/graphs'.format(pixela_url, user)

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# print(response.text)

pixel_endpoint = '{}/{}/graphs/{}'.format(pixela_url, user, graph_params['id'])

today = datetime(year=2021, month=12, day=23)
the_today = today.strftime('%Y%m%d')

pixel_params = {
    'date':the_today,
    'quantity':'8',
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

print(response.text)