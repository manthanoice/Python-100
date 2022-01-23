import requests
import ast

def age(name):
    response = requests.get(url='https://api.agify.io/?name={}'.format(name))
    the_age = response.text
    return ast.literal_eval(the_age)['age']

def gender(name):
    response = requests.get(url='https://api.genderize.io/?name={}'.format(name))
    the_gender = response.text
    return ast.literal_eval(the_gender)

print(age('Manthan'))
print(gender('manthan'))