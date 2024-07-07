import csv

from flask import Flask, render_template, redirect, url_for, request
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
                                choices=[(1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')])
    wifi_rating = SelectField('Wifi Rating', validators=[DataRequired()],
                              choices=[(1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    power = SelectField('Power Socket Availability', validators=[DataRequired()],
                        choices=[(1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == "POST" and form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as file:
            file.write(f"{form.cafe.data}, {form.location_url.data}, {form.opening.data}, {form.closing.data},"
                       f" {form.coffee_rating.data}, {form.wifi_rating.data}, {form.power.data}\n")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = []
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data)

        for row in data:
            list_of_rows.append(
                {
                    "name": row[0],
                    "location": row[1],
                    "opening": row[2],
                    "closing": row[3],
                    "coffee": row[4],
                    "wifi": row[5],
                    "power": row[6]
                }
            )
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
