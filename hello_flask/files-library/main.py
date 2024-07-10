from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
# from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.secret_key = "mysecret"


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# ma = Marshmallow(app)
bootstrap = Bootstrap5(app)


## Create a new table in the database
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # this will allow each book to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}>'

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
