from flask import Flask, render_template
import requests
import json

def age(name):
    response = requests.get(url='https://api.agify.io/?name={}'.format(name))
    the_age = response.text
    return json.loads(the_age)['age']

def gender(name):
    response = requests.get(url='https://api.genderize.io/?name={}'.format(name))
    the_gender = response.text
    return json.loads(the_gender)['gender']

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hey in the URL above after the "/" enter your name and it will predict your age and gender ;)</h1>'

@app.route('/<yourname>')
def your_name(yourname):
    your_age = age(yourname)
    your_gender = gender(yourname)
    return render_template('agender.html', the_name=yourname, the_age = your_age, the_gender = your_gender)

if __name__ == '__main__':
    app.run(debug=True)