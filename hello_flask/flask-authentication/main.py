from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# create a user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# fixing table in database with the UserMixin
class User(UserMixin, db.Model):
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
        # hashing and salting the password
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # sorting the hashed password in the database
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name')
        )
        # does email exists?
        user = User.query.filter_by(email=new_user.email).first()
        if user:
            return 'User with that email already exists!', 400

        db.session.add(new_user)
        db.session.commit()

        # login and authenticate the user after adding details to the database
        login_user(new_user)

        #can redirect() and get name from the current_user
        return redirect(url_for('secrets'))
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # check if email exists
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            return 'User does not exist!', 400

        # check if password is correct
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template('login.html')


@app.route('/forgot')
def forgot_pass():
    pass


@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html', name=current_user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == '__main__':
    app.run(debug=True)
