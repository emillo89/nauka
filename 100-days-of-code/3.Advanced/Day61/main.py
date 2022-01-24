from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import os

class Form(FlaskForm):
    email = StringField(label='email')
    password = PasswordField(label='password')
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = os.environ["PASSWORD"]

# home page
@app.route("/")
def home():
    return render_template('index.html')

# login page
@app.route("/login")
def login():
    form = Form()
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)