from datetime import date, datetime

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import login_user, current_user, LoginManager, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.testing.plugin.plugin_base import logging
from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm, ContactForm, CreatePostForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
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


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
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
    comments = relationship('Comment', back_populates='post')  # create a relationship with the Comment table


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
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False, default=date.today().strftime('%B %d, %Y'))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('blog_posts.id'), nullable=False)


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


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    if form.validate_on_submit():
        new_comment = Comment(
            name=form.name.data,
            text=form.comment.data,
            date=datetime.now().strftime('%B %d, %Y'),
            post_id=post_id
        )
        try:
            db.session.add(new_comment)
            db.session.commit()
            flash("Comment added successfully!", 'success')
            return redirect(url_for('show_post', post_id=post_id))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"There was an issue adding your comment. Please try again. {str(e)}", 'danger')
    else:
        print(form.errors)
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('post.html', post=requested_post, form=form, comments=comments)


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
        except SQLAlchemyError as e:
            logging.error(f"There was an issue adding the post: {e}")
            db.session.rollback()
            flash("There was an issue adding your post. Please try again.")
            return redirect(url_for('add_new_post'))
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, is_edit=False)


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
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
        post.author = current_user.name
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=edit_form, is_edit=True)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_to_delete = db.session.execute((db.select(BlogPost).where(BlogPost.id == post_id))).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
