from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnFraWRmdnI0NnF1Z3A0anIzNG9scnU0aXR1YXB6N2Fza2x2ejg5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.webp'>"


if __name__ == "__main__":
    app.run(debug=True)

hello()
