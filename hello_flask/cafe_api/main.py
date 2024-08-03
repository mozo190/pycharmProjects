from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


# Create a new table in the database
class Base(DeclarativeBase):
    pass


# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe table configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=False)


# HTTP GET - Read Record
# HTTP POST - Create Record
# HTTP PUT/PATCH - Update Record
# HTTP DELETE - Delete Record

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
