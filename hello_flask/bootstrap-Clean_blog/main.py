import requests
from flask import Flask, render_template

app = Flask(__name__)

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_api)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
