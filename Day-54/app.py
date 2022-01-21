from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Bitches'

@app.route('/bye')
def bye_world():
    return 'Bye bitches'

if __name__ == '__main__':
    app.run()