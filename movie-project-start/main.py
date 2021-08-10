from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Database
db = SQLAlchemy(app)
class Movie(db.Model):
   id = db.Column('movie_id', db.Integer, primary_key = True)
   title= db.Column(db.String(100))
   year = db.Column(db.Integer)
   description = db.Column(db.Integer)
   rating = db.Column(db.Integer)
   ranking= db.Column(db.Integer)
   review = db.Column(db.String(500))
   img_url= db.Column(db.String(500))
   def _init_(self, title,year,description,rating,ranking,review,img_url):
    self.title = title
    self.year  = year 
    self.description =description 
    self.rating  = rating 
    self.ranking= ranking
    self.review= review
    self.img_url= img_url
db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()
#Flask Form
class AddMovie(FlaskForm):
    id = StringField('Movie Id', validators=[DataRequired()])
    title= StringField('Movie Title', validators=[DataRequired()])
    year= StringField('year', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    review= StringField('review', validators=[DataRequired()])
    ranking = StringField('ranking', validators=[DataRequired()])
    img_url = StringField('img_url', validators=[DataRequired()])
    submit = SubmitField('Submit')
class RateMovieForm(FlaskForm):
    rating = StringField('Your ratinf out of 10', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')
@app.route("/")
def home():
    m=Movie.query.all()
    for a in m:
        print(a.title)
    return render_template("index.html",movies = Movie.query.all())

@app.route("/add",methods=["POST","GET"])
def add():
    form = AddMovie()
    id = form.id.data
    title = form.title.data
    year= form.year.data
    description = form.description.data
    rating = form.rating.data
    review = form.review.data
    ranking = form.ranking.data
    img_url= form.img_url.data
    if form.validate_on_submit():
      new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url
    )
      db.session.add(new_movie)
      db.session.commit()
      return redirect(url_for('home'))
    return render_template("add.html",form=form)
@app.route("/edit/<movie_id>",methods=["POST","GET"])
def edit(movie_id):
    form= RateMovieForm()
    rating= form.rating.data
    review = form.review.data
    if form.validate_on_submit():
        movie_to_update= Movie.query.get(movie_id)
        movie_to_update.rating =rating
        movie_to_update.review=review
        db.session.commit()
        return redirect(url_for('home'))
    movie_selected =Movie.query.get(movie_id)
    return render_template("edit.html", form=form)
@app.route("/delete/<movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))
if __name__ == '__main__':
    app.run(debug=True)
