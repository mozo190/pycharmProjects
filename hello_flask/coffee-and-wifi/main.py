from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time', validators=[DataRequired()])
    closing = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()],
                                choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    wifi_rating = SelectField('Wifi Rating', validators=[DataRequired()],
                              choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    power = StringField('Power Socket Availability', validators=[DataRequired()])
    submit = SubmitField('Submit')
