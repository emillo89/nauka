from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

#new Database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.rating}"

db.create_all()

#new record
# book1 = Book(title="Kevin sam w domu", author="Nieznany", rating=9)
# db.session.add(book1)
# db.session.commit()

#read
all_books = Book.query.all()
print(all_books)

# book = Book.query.filter_by(title="Kevin sam w domu").first()
# print(book)

#Update
# book_to_update = Book.query.filter_by(title="Kevin sam w domu").first()
# book_to_update.title = "Kevin"
# db.session.commit()

#Update a record by PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Kevin sam"
# db.session.commit()

#Delete a particular record by PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
