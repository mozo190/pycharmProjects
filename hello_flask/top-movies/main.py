import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.testing import db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("mysecret")
Bootstrap5(app)

class Base(DeclarativeBase):
    pass


# Create a new table in the database
class Movie(db.Model):
    pass
