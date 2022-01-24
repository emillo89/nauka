from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

class Form(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")

app = Flask(__name__)
app.secret_key = os.environ["PASSWORD"]

# home page
@app.route("/")
def home():
    return render_template('index.html')

# login page
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Form()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == "yourname@gmail.com" and form.password.data == "test1234":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)