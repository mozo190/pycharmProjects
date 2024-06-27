from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello you little {name}!"

if __name__ == "__main__":
    app.run(debug=True)

greet("Krisztián")

# def outer_function():
#     print("I'm outer f")
#
#     def nested_function():
#         print("I'm inner f")
#
#     return nested_function
#
#
# inner_f = outer_function()
#
# inner_f()
