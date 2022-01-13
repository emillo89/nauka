from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

post_object = []
response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
for post in response:
    # print(post)
    new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_object.append(new_post)

@app.route('/')
def home():
    return render_template("index.html", post=post_object)

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in post_object:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
