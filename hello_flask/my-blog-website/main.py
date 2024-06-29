import requests
from flask import Flask, render_template
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
post_objects = []
for post in posts.json():
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:index>")
def blog():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
