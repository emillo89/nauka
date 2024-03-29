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

@app.route('/post/<int:index>')
def show_posts(index):
    requests_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requests_post = blog_post
    return render_template("posts.html", post=requests_post)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")