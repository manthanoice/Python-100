from flask import Flask, render_template
import requests

app = Flask(__name__)

all_response = requests.get(url='https://api.npoint.io/e4b5fedd96faddb691d0').json()
the_length = len(all_response)

@app.route('/')
def home():
    return render_template("index.html", blog_post = all_response, the_num = the_length)

@app.route('/post/<int:num>')
def the_body(num):
    return render_template('post.html', blog_post = all_response[num])

if __name__ == "__main__":
    app.run(debug=True)