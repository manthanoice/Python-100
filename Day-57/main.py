from flask import Flask, render_template
import requests
import random
from datetime import datetime
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
    curret_year = datetime.now().year
    random_number = random.randint(1, 10000)
    return render_template('index.html', num=random_number, the_year=curret_year)

@app.route('/<yourname>')
def your_name(yourname):
    your_age = age(yourname)
    your_gender = gender(yourname)
    return render_template('agender.html', the_name=yourname, the_age = your_age, the_gender = your_gender)

@app.route('/blog/<num>')
def get_to_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/e4b5fedd96faddb691d0'
    response = requests.get(url=blog_url).text
    all_response = json.loads(response)
    return render_template('blog.html', posts = all_response)

if __name__ == '__main__':
    app.run(debug=True)