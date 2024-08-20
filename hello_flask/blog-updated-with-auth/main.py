from datetime import date

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import login_user, current_user, LoginManager, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm, ContactForm, CreatePostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# Create a database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app, model_class=Base)

# configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# create a user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# Create a table in database
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


with app.app_context():
    db.create_all()


# use werkzeug.security to hash and salt the password when a user registers
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # hash and salt the password
        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            password=hash_and_salted_password,
            name=form.name.data
        )
        db.session.add(new_user)
        db.session.commit()

        # login the user after successful registration
        login_user(new_user)

        return redirect(url_for('get_all_posts'))

    return render_template('register.html', form=form)


# retrieve a user from the database based on their email address
# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = StringField("Password", validators=[DataRequired()])
#     submit = StringField("Log In")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again!")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, request.form.get('password')):
            flash('Password incorrect, please try again!')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template('login.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
@login_required
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.date.desc()))
    posts = result.scalars().all()
    return render_template('index.html', all_posts=posts, logged_in=True)


@app.route('/new_post', methods=['GET', 'POST'])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.name,
            date=date.today().strftime('%B %d, %Y')
        )
        try:
            db.session.add(new_post)
            db.session.commit()
        except:
            print("There was an issue adding your post")
            db.session.rollback()
            return redirect(url_for('new_post'))
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, is_edit=False)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
