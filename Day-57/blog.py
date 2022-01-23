from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hehe'

if __name__ == '__main__':
    app.run(debug=True)