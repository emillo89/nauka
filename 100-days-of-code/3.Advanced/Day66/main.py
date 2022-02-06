import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    #another metod of serialising our database
    def to_dict(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")


#Take random row in database
@app.route("/random")
def get_random_data():
    cafes = db.session.query(Cafe).all()
    cafe_random = random.choice(cafes)
    return jsonify(cafe={"id": cafe_random.id,
                    "name": cafe_random.name,
                    "map_url": cafe_random.map_url,
                    "img_url": cafe_random.img_url,
                    "location": cafe_random.location,
                    "has_sockets": cafe_random.has_sockets,
                    "has_toilet": cafe_random.has_toilet,
                    "has_wifi": cafe_random.has_wifi,
                    "can_take_calls": cafe_random.can_take_calls,
                    "seats": cafe_random.seats,
                    "coffee_price": cafe_random.coffee_price})


    #return with dict
    # return jsonify(cafe=cafe_random.to_dict())



## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
