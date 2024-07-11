from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
# from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError
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
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # this will allow each book to be identified by its title when printed
    # def __repr__(self):
    #     return f'<Book {self.title}>'

    # create table schema in the database. Required application context
    with app.app_context():
        db.create_all()


# Create a new record in the database
with app.app_context():
    new_book = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
    try:
        db.session.add(new_book)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print(f"Book already exists in the database: {e}")


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_book_sample = {
            "title": title,
            "author": author,
            "rating": rating
        }
        db.session.add(new_book_sample)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
