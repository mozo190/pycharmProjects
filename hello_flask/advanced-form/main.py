from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

app = Flask(__name__)
app.secret_key = "mysecret"


class MyForm(FlaskForm):
    name = StringField('Email', validators=[DataRequired(), Email()])  # StringField('Name
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=19)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Log In')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.name.data
        password = form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html", name=email, password=password)
        else:
            return render_template("denied.html", form=form)
    return render_template("login.html", form=form)


@app.route('/submit', methods=["GET", "POST"])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('submit.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
