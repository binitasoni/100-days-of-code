from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

import datetime

## Delete this code:
# import requests
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
    body = CKEditorField('Body')
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    post_list = []
    post_query = db.session.query(BlogPost).all()
    for post in post_query:
     if post:
        post_dict = {"id": post.id, "title": post.title, "subtitle": post.subtitle,
                     "date": post.date,
                     "body": post.body, "author": post.author,
                     "img_url": post.img_url
                     }
        post_list.append(post_dict)
    posts =post_list
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    post_list=[]
    post_query = db.session.query(BlogPost).all()
    for post in post_query:
        if post:
            post_dict = {"id": post.id, "title": post.title, "subtitle": post.subtitle,
                         "date": post.date,
                         "body": post.body, "author": post.author,
                         "img_url": post.img_url
                         }
            post_list.append(post_dict)
    posts =post_list
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
@app.route('/delete/<post_id>')
def delete(post_id):
    post= BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/edit_post")
def edit_post():
    pass

@app.route("/new-post",methods=["POST","GET"])
def new_post():
    form = CreatePostForm()
    date=datetime.date.today().strftime("%B %d, %Y")
    if request.method == 'POST':
        new_post=BlogPost(
        title=request.form.get("title"),
        subtitle = request.form.get("subtitle"),
        author = request.form.get("author"),
        img_url = request.form.get("img_url"),
        date=date,
        body = request.form.get("body")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html",form=form)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)