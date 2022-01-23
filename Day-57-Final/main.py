from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

all_response = requests.get(url='https://api.npoint.io/e4b5fedd96faddb691d0').json()

@app.route('/')
def home():
    return render_template("index.html", blog_post = all_response)

@app.route('/post/<int:num>')
def the_body(num):
    return render_template('post.html', blog_post = all_response[num])

if __name__ == "__main__":
    app.run(debug=True)