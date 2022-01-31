import smtplib

from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

posts = requests.get("https://api.npoint.io/e75317e81f55868d3766").json()

MY_EMAIL = "appbrewery5@gmail.com"

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, phone, email, message)
        return render_template("contact.html", msg_send=True)
    return render_template('contact.html', msg_send=False)

@app.route('/post/<int:index>')
def post(index):
    request_post=None
    for blog_post in posts:
        if blog_post['id'] == index:
            request_post = blog_post
    return render_template('post.html', post=request_post)

def send_email(name, phone, email, message):
    with smtplib.SMTP("smtp.gmail.com") as conenction:
        message = f"Subject message\nName: {name}\nPhone: {phone}\nEmail: {email}\nMessage:{message}"
        conenction.starttls()
        conenction.login(MY_EMAIL, MY_PASSWORD)
        conenction.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)

if __name__ == "__main__":
    app.run(debug=True)