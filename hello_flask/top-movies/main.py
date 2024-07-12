import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("mysecret")
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
    with app.app_context():
        db.create_all()

# Create a new record in the database
with