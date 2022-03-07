from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potterrrr', 'J. K. Rowling', '9.3')")
db.commit()

all_books = []

@app.route('/')
def home():
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title":request.form["title"],
            "author":request.form["author"],
            "rating":request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)