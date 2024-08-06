from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    all_post = BlogPost.query.all()
    return render_template('index.html', posts=all_post)


# a route so that you can click in individual post
@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template('post.html', post=requested_post)


# add_new_post to create a new post
@app.route('/new_post')
def add_new_post():
    return render_template('make-post.html')


# edit_post to edit a post
@app.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template('edit-post.html', post=requested_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=5003)
