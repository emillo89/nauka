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


#Take all rows
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify(all_cafe=[cafe.to_dict() for cafe in cafes])
    #different metod to show all rows
    # cafe_list = []
    # for cafe in cafes:
    #     cafe_dict = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url,
    #                  "img_url": cafe.img_url,
    #                  "location": cafe.location, "has_sockets": cafe.has_sockets,
    #                  "has_toilet": cafe.has_toilet, "has_wifi": cafe.has_wifi,
    #                  "can_take_calls": cafe.can_take_calls, "seats": cafe.seats,
    #                  "coffee_price": cafe.coffee_price}
    #     cafe_list.append(cafe_dict)
    # all_cafes = {"cafes": cafe_list}
    # all_cafes_json = jsonify(cafes=all_cafes["cafes"])
    # return all_cafes_json


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        location = request.form["location"]
        cafes = db.session.query(Cafe).filter_by(location=location)
        if cafes:
            return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
        else:
            return jsonify(error={"Not Found" : "Sorry, we don't have cafe at the location"})
    return render_template("search.html")

#alternative method to add new Cafes and we should to add make bool before boolean atributes
#e.g has_sockets = make_bool(request.form["has_sockets"])
# def make_bool(val: int) -> bool:
#     return bool(int(val))


#add new cafe
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        new_cafes = Cafe(
            name = request.form["name"],
            map_url = request.form["map_url"],
            img_url = request.form["img_url"],
            location = request.form["location"],
            has_sockets = int(request.form["has_sockets"]),
            has_toilet = int(request.form["has_toilet"]),
            has_wifi = int(request.form["has_wifi"]),
            can_take_calls = int(request.form["can_take_calls"]),
            seats = request.form["seats"],
            coffee_price = request.form["coffee_price"]
        )

        db.session.add(new_cafes)
        db.session.commit()
        return jsonify({"response":{"success": "Success added the new cafe."}})
    return render_template("add.html")
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
