from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def login():
    # return "💪 Success! Form submitted"
    username = request.form["name"]
    password = request.form["password"]
    return f"💪 Success! Form submitted by {username} with password {password}"
    # render_template("login.html", name=username, password=password))


if __name__ == "__main__":
    app.run(debug=True)
