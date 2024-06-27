import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


rand_num = random.randint(0, 9)


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > rand_num:
        return "<h1 style='color: red'>Too high, try again!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=1200>"
    elif guess < rand_num:
        return "<h1 style='color: purple'>Too low, try again!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=1200>"
    else:
        return "<h1 style='color: green'>You found me!</h1>'<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='1200'>"


if __name__ == "__main__":
    app.run(debug=True)

hello()
