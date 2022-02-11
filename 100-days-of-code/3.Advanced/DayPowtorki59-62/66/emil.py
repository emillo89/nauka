from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def home():
    return render_template('index.html')

#2 wykorzystanie session
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["first_name"]
        session["user"] = user
        flash(f"Login Successfull: {user}")
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash(f"Already Logged In!")
            return redirect(url_for('user'))
        else:
            return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        user = session["user"]
        return render_template(url_for('user', user=user))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"You have been logged out, {user} !", "info")
    session.pop('user',None)
    return redirect(url_for('login'))


#1.jak odniesc sie do usera
# @app.route('/login',methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         user = request.form["first_name"]
#         return redirect(url_for('user', usr=user))
#     else:
#         return render_template('login.html')
#
#
# @app.route('/<usr>')
# def user(usr):
#     return f"<h1> {usr} </h1>"


# @app.route('/')
# def home():
#     return "Hello! this is new sentence."
#
#
# @app.route('/<name>')
# def user(name):
#     return f"Hello {name}"
#
# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin'))

if __name__ == "__main__":
    app.run(debug=True)