import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    current_year = datetime.datetime.now().year
    random_number = random.randint(0, 9)
    return render_template("index.html", number=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    capitalized_name = name.capitalize()
    data = response.json()
    data_gender = response_gender.json()
    get_gender = data_gender["gender"]
    get_age = data["age"]
    return render_template("guess.html", name=capitalized_name, gender=get_gender, age=get_age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
