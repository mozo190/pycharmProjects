from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.secret_key = "mysecret"


class MyForm(FlaskForm):
    name = StringField('name')
    password = PasswordField('password')
    submit = SubmitField('submit')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        return f"💪 Success! Form submitted by {username} with password {password}"
    return render_template("login.html", form=form)


@app.route('/submit', methods=["GET", "POST"])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('submit.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
