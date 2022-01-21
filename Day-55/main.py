from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inside():
        return "<b>"+function()+"</b>"
    return inside

def make_italic(function):
    def inside():
        return "<em>"+function()+"</em>"
    return inside

def make_underline(function):
    def inside():
        return "<u>"+function()+"</u>"
    return inside

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello there, hehe</h1>' \
    '<p>This is a para lmfao</p>'\
    '<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width=200>'

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def say_bye():
    return 'Bye Lmao'

@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return 'Hello there {}, seems like you are {} years old'.format(name, age)

if __name__ == '__main__':
    app.run(debug=True)