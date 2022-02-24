from flask import Flask, render_template

app = Flask(__name__)

"""Filters:
safe
capitalize
lower
upper
title
trim
striptags"""


@app.route('/')
def home():
    stuff = 'This is <strong> Bold </strong>'
    title = "This is bold text"
    favourite_pizza = ["Margerita", "Pepperoni", 41]

    return render_template('index.html',
                           stuff=stuff,
                           title=title,
                           favourite_pizza=favourite_pizza)

# @app.route('/<name>')
# def user(name):
#     return render_template('user.html', user_name=name)


#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


#Invalid Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)