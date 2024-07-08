from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
# from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "mysecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# ma = Marshmallow(app)
bootstrap = Bootstrap5(app)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = {
            "title": title,
            "author": author,
            "rating": rating
        }
        all_books.append(new_book)
        return redirect("/")
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
