from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"Book {Book.title}"
db.create_all()

#CREATE RECORD
first_book = Book(title="Harry Potter", author="J.K.Rowling", rating=9.3)
db.session.add(first_book)
db.session.commit()