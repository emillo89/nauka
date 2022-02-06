from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MyForm(Form):
    rating = StringField("Your Rating Our of 10 e.g. 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")

#Create table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(256), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(256), nullable=True)
    img_url = db.Column(db.String(256), nullable=False)

db.create_all()

#After adding the new_movie code needs to be commented, not trying to add the same movie twice
# new_movie = Movies(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepeard finds himself trapped in a phone",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#
#     )
#
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies = Movies.query.all()
    print(all_movies)
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MyForm()
    # movie_id = request.args.get("id")
    # movie = Movies.query.get(movie_id)
    # if form.validate_on_submit():
    #     movie.rating = float(form.rating.data)
    #     movie.review = form.review.data
    #     db.session.commit()
    #     return redirect(url_for('home'))
    return render_template("edit.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
