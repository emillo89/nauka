import requests
from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")