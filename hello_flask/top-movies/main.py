import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_SECRET")
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


# Configure the database - db is an instance of SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Create a new table in the database
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # this will allow each movie to be identified by its title when printed
    def __repr__(self):
        return f'<Movie {self.title}>'

    # create table schema in the database. Required application context


# Create a new record in the database
with app.app_context():
    db.create_all()
    new_movie = Movie(title="Harry Potter",
                      year=2001,
                      description="Harry Potter and the Philosopher's Stone",
                      rating=7.6,
                      ranking=1,
                      review="Harry Potter is a great movie",
                      img_url="https://www.imdb.com/title/tt0241527/"
                      )
    try:
        db.session.add(new_movie)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        print("Movie already exists in the database")


# Home route
@app.route('/')
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
