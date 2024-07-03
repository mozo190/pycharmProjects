import requests
from flask import Flask, render_template

app = Flask(__name__)

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_api)
post_objects = []
for post in response.json():
    post_obj = {
        "id": post["id"],
        "title": post["title"],
        "subtitle": post["subtitle"],
        "body": post["body"]
    }
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
