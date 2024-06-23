from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


def outer_function():
    print("I'm outer f")

    def nested_function():
        print("I'm inner f")

    return nested_function


inner_f = outer_function()

inner_f()
