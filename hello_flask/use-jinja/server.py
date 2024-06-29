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
    capitalized_name = name.capitalize()
    data = response.json()
    get_gender = data["age"]
    get_age = "Unknown"
    return render_template("guess.html", name=capitalized_name, gender=get_gender, age=get_age)


if __name__ == "__main__":
    app.run(debug=True)
