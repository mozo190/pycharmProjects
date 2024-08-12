from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' 


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        new_user = User(
            email=request.form.get('email'),
            password=request.form.get('password'),
            name=request.form.get('name')
        )
        # does email exists?
        user = User.query.filter_by(email=new_user.email).first()
        if user:
            return 'User with that email already exists!', 400

        db.session.add(new_user)
        db.session.commit()

        # passing over the user's name to the secrets.html
        return render_template('secrets.html', name=request.form.get('name'))
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/forgot')
def forgot_pass():
    pass


@app.route('/secrets')
def secrets():
    return render_template('secrets.html')


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == '__main__':
    app.run(debug=True)
