from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# config table
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False, default=datetime.now().strftime('%B %d, %Y'))
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Post Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Post Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_post = result.scalar().all()
    return render_template('index.html', posts=all_post)


# a route so that you can click in individual post
@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    return render_template('post.html', post=requested_post)


# add_new_post to create a new post
@app.route('/new_post', methods=['GET', 'POST'])
def add_new_post():
    if request.method == 'POST':
        new_post = BlogPost(
            title=request.form['title'],
            subtitle=request.form['subtitle'],
            date=datetime.now().strftime('%B %d, %Y'),
            body=request.form.get('body', ""),
            author=request.form.get('author', 'Anonymous'),
            img_url=request.form['img_url']
        )
        try:
            db.session.add(new_post)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("Post already exists in the database", 400)
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html')


# edit_post to edit a post
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    # post_id = request.args.get('post_id')
    requested_post = BlogPost.query.get_or_404(post_id)
    if request.method == 'POST':
        requested_post.title = request.form['title']
        requested_post.subtitle = request.form['subtitle']
        requested_post.date = request.form['date']
        requested_post.body = request.form['body']
        requested_post.author = request.form['author']
        requested_post.img_url = request.form['img_url']
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', post=requested_post, editing=True)


# delete_post to delete a post from database
@app.route('/delete_post', methods=['POST'])
def delete_post():
    post_id = request.form['post_id']
    if not post_id:
        return "Post not exist in the database"
    post_to_delete = BlogPost.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=5003)
