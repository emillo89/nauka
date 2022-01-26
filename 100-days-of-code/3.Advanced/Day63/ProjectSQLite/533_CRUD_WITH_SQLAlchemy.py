from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emil.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Create Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

#New record

# new_book = Book(title="Harry Potter", author="J.K.Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

#Read all books
# all_books = session.query(Book).all()
# print(all_books)

#Read a particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# print(Book.query.all())

#Update a particular record by Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

#update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter"
# db.session.commit()

#Delete a particular record by primary key
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()