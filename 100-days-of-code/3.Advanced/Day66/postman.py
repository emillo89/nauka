import random

from flask import Flask, jsonify, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"

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


#Take all rows
@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify(all_cafe=[cafe.to_dict() for cafe in cafes])


@app.route("/search/<string:location>", methods=["GET"])
def search():
    location = request.args.get('location')
    cafes = db.session.query(Cafe).filter_by(location=location)
    print(cafes)
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes if cafe['location'] == location])
    else:
        return jsonify(error={"Not Found" : "Sorry, we don't have cafe at the location"})



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


#edit row in database
@app.route('/update-price', methods=["GET","POST"])
def new_price():
    if request.method == "POST":
        cafe_id = request.form["id"]
        print(cafe_id)
        new_price = request.form["new_price"]
        print(new_price)
        cafe = db.session.query(Cafe).get(cafe_id)
        print(cafe)
        if cafe:
            print("Ok")
            cafe.coffee_price = new_price
            print(cafe.coffee_price)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"})
    else:
        return render_template('edit.html')


@app.route('/cafe-deleted',methods=['GET', 'POST'])
def delete_cafe():
    if request.method == 'POST':
        cafe_id = request.form['id']
        deleted_cafe = db.session.query(Cafe).get(cafe_id)
        if deleted_cafe:
            db.session.delete(deleted_cafe)
            db.session.commit()
            return jsonify(response={'Success': 'Successfully deleted the cafe with the detabase '})
        else:
            return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database'})

    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
