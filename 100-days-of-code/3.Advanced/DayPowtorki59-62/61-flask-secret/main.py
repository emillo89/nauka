from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "emil"
Bootstrap(app)

class Form(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=4, max=8)])
    submit = SubmitField(label="log in")


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    form = Form()
    if form.validate_on_submit():
        if form.email.data == "name@gmail.com" and form.password.data == "test1234":
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)