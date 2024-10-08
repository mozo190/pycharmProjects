import os
from datetime import date
from functools import wraps

from flask import Flask, render_template, flash, redirect, url_for, abort
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import login_user, current_user, LoginManager, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm, CreatePostForm, CommentForm, ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap5(app)

# configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# create a user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# for adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# Create a database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///posts.db')
db = SQLAlchemy(app, model_class=Base)


# Create a table in database
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))  # create a foreign key to the User table
    author = relationship('User', back_populates='posts')

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship('Comment', back_populates='parent_post', cascade="all, delete", lazy=True)  # create a relationship with the Comment table


# create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    posts = relationship('BlogPost', back_populates='author')  # create a relationship with the BlogPost table
    comments = relationship('Comment', back_populates='comment_author')  # create a relationship with the Comment table


class Comment(db.Model):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    comment_author = relationship('User', back_populates='comments')
    post_id: Mapped[str] = mapped_column(Integer,
                                         db.ForeignKey('blog_posts.id'))  # create a foreign key to the BlogPost table
    parent_post = relationship("BlogPost", back_populates='comments')


with app.app_context():
    db.create_all()


# create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:  # check if the current user is the admin
            return abort(403)
        return f(*args, **kwargs)  # if the user is the admin, return the original function

    return decorated_function


# use werkzeug.security to hash and salt the password when a user registers
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        result = db.session.execute(db.select(User).where(User.email == form.email.data))
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

    return render_template('register.html', form=form, current_user=current_user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again!")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again!')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template('login.html', form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template('index.html', all_posts=posts, current_user=current_user)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to log in or register to comment.")
            return redirect(url_for('login'))

        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()
    return render_template('post.html', post=requested_post, form=form, current_user=current_user)


@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, current_user=current_user)


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('make-post.html', form=edit_form, is_edit=True, current_user=current_user)


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/about')
def about():
    return render_template('about.html', current_user=current_user)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact', msg_sent=True))
    return render_template('contact.html', form=form, msg_sent=False, current_user=current_user)


if __name__ == "__main__":
    app.run(debug=False, port=5002)
