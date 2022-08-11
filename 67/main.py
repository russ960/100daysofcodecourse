from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


## Delete this code:
import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    # requested_post = None
    # posts = BlogPost.query.all()
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    requested_post = BlogPost.query.filter_by(id=index).first()
    return render_template("post.html", post=requested_post)

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    return render_template("make-post.html", form=form, source="new")

@app.route('/edit-post/<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    form = CreatePostForm()
    if request.method == 'GET':
        # Populate the form.
        
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.author.data = post.author
        form.img_url.data = post.img_url
        form.body.data = post.body
        return render_template("make-post.html", form=form, source="edit")
    if request.method == 'POST':
        post.title = request.form["title"]
        post.subtitle = request.form["subtitle"]
        post.author = request.form["author"]
        post.img_url = request.form["img_url"]
        # post.body = request.form["body"]
        post.body = form.body.data
        db.session.commit()
        return redirect(f"/post/{post_id}")
    
@app.route('/delete/<int:post_id>', methods=["GET"])
def delete_post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    if post:
        post.query.filter_by(id=post_id).delete()
        db.session.commit()   
    return redirect(f"/")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)