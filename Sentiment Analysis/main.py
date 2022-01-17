from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from flask_wtf import FlaskForm
import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
bootstrap = Bootstrap(app)
#FORM
class UploadForm(FlaskForm):
  text_content = TextAreaField("Enter Text")
  submit = SubmitField("Submit")
  download = SubmitField("Download")

#MODEL
dataset_new = pd.read_csv(r"C:\Users\Shruti Soni\Downloads\smile-annotations-final.csv",encoding='latin-1')
def sentiment_detection(text):
  X_train, X_test, y_train, y_test = train_test_split(dataset_new['Tweet'], dataset_new['feeling'],
                                                      random_state=4)
  count_vect = CountVectorizer()
  X_train_counts = count_vect.fit_transform(X_train.values.astype('str'))
  tfidf_transformer = TfidfTransformer()
  X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
  X_test_counts = count_vect.fit_transform(X_test.values.astype('str'))
  X_test_tfidf = tfidf_transformer.fit_transform(X_test_counts)
  model = LinearSVC()
  model.fit(X_train_tfidf, y_train)
  clf = LinearSVC().fit(X_test_tfidf, y_test)
  cat = clf.predict((count_vect.transform([text])))
  return cat[0]
@app.route('/', methods=["GET", "POST"])
def index():
  form = UploadForm()
  sentiment=""
  if request.method == "POST":
    if form.validate_on_submit():
      text=form.text_content.data
      sentiment=sentiment_detection(text)
  return render_template("index.html", form=form,sentiment=sentiment)


if __name__ == "__main__":
  app.run(debug=True)
#create a sentiment analysis model
#Ask for input of text from user
#return back the model