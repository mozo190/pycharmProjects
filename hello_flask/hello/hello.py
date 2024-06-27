from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f'<b>' + func() + '</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f'<em>' + func() + '</em>'
    return wrapper

def make_underlined(func):
    def wrapper():
        return f'<u>' + func() + '</u>'
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return (
        f'<h2 style="text-align: center; background: black; color: white" >Hello you little {name} you are {number} years old!</h2>' \
        '<p style="text-align: center">This is a paragraph.</p>'
        '<div style="text-align:center"><img src="https://cdn.britannica.com/34/235834-050-C5843610/two-different-breeds-of-cats-side-by-side-outdoors-in-the-garden.jpg" width=1200></div>')


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
