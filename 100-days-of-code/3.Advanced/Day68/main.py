from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


#Register new users
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form['email']).first():
            #User already exists
            flash(f"You've already signed up with that email, log in instead")
            return redirect(url_for('login'))
        hash_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8 )
        new_user = User(
            email=request.form["email"],
            password=hash_password,
            name=request.form["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template('secrets.html',name=new_user.name)
    return render_template("register.html", logged_id=current_user.is_authenticated)


#login on your account
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email=request.form["email"]
        password=request.form["password"]

        #Find user by email entered
        user = User.query.filter_by(email=email).first()

        if not user:
            flash(f"That email does not exists, please try again.")
            return redirect(url_for('login'))
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(user.password, password):
            flash(f"Password incorrect,please try again.")
            return redirect(url_for('login'))
        else:
            #authentication user
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


#logout with your account
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


#download files
@app.route('/download')
@login_required
def download():
    return send_file('static/files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
