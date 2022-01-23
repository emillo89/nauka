import smtplib
import requests
from flask import Flask, render_template, request
import os

MY_EMAIL = os.environ["MY_EMAIL"]


app = Flask(__name__)

#link to my npoint
posts = requests.get("https://api.npoint.io/711a742141f41dfdeaec").json()
print(posts)

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_posts(index):
    requests_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requests_post = blog_post
    return render_template("posts.html", post=requests_post)

@app.route('/form-entry', methods=['POST'])
def form_data():
    name = request.form["username"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    send_email(email, phone, message)
    return "<h1> Successfully send your message </h1>"


def send_email(email, phone, message):
    MY_PASSWORD = os.environ["MY_PASSWORD"]
    email_message = f"Subject:New Message\n\nName\n Email: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")