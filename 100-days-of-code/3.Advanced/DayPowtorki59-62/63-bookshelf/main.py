from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# new Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#new Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()



@app.route('/')
def home():
    all_books = Book.query.all()
    print(all_books)
    return render_template("index.html", posts=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        book = Book(
            title = title,
            author = author,
            rating = rating
        )

        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form['id']
        book_to_change = Book.query.get(book_id)
        book_to_change.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)

    return render_template("edit-rating.html", selected=book_selected)


@app.route('/delete/')
def delete():
    book_id = request.args.get('id')
    print(book_id)

    #delete a record by id
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

