from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    current_year = datetime.datetime.now().year
    random_number = random.randint(0, 9)
    return render_template("index.html", number=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
