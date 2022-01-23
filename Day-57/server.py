from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    curret_year = datetime.now().year
    random_number = random.randint(1, 10000)
    return render_template('index.html', num=random_number, the_year=curret_year)

if __name__ == '__main__':
    app.run(debug=True)