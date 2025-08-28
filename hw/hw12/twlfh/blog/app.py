from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'
# Configure the SQLAlchemy database URI. You should replace 'sqlite:///posts.db' with your actual database URI.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


# Define the Post model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if post:
        return render_template('post.html', post=post)
    else:
        abort(404)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = Post.query.get(id)
    if not post:
        abort(404)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('"{}" was successfully deleted!'.format(post.title))
        return redirect(url_for('index'))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(port=5000)
