from flask import Flask
import random

random_number = random.randint(1, 9)

found_me = "https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif"
too_high = "https://media.giphy.com/media/YNPjwaQdIb3K8/giphy.gif"
tooo_low = "https://media.giphy.com/media/U3PFGB8kCBVf7EN4Fk/giphy.gif"

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
def function(num):
    if num > 9:
        return '<h1> Please enter number between 1 and 9 only, thank you </h1>'
    if num > random_number:
        return '<h1>Too high</h1>'\
        '<img src="{}" width=300 height=300>'.format(too_high)
    if num < random_number:
        return '<h1>Too low</h1>'\
        '<img src="{}" width=300 height=300>'.format(tooo_low)
    if num == random_number:
        return '<h1>Found me</h1>'\
        '<img src="{}" width=300 height=300>'.format(found_me)

if __name__ == '__main__':
    app.run(debug=True)