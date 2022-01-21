from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello There'

@app.route('/bye')
def bye_world():
    return 'Bye There :P'

if __name__ == '__main__':
    app.run()