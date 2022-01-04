import colorgram
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from flask_wtf import FlaskForm
import os


def color_generator(image_file_name):
 rgb = []
 d=colorgram.extract(image_file_name, 7)
 for colors in d:
  r=colors.rgb.r
  b=colors.rgb.b
  g=colors.rgb.g
  a=(r,g,b)
  rgb.append(a)
 return rgb

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
bootstrap = Bootstrap(app)
class UploadForm(FlaskForm):
  file = FileField()
  submit = SubmitField("Submit")
  download = SubmitField("Download")


@app.route('/', methods=["GET", "POST"])
def index():
  form = UploadForm()
  if request.method == "POST":

    if form.validate_on_submit():
      file_name = form.file.data
      print(file_name)
      file_name.save(os.path.join(r"C:\Users\Shruti Soni\PycharmProjects\pythonProject3", file_name.filename))
      rgb=color_generator(file_name.filename)
      print(rgb)
      return render_template("color.html", len = len(rgb), rgb = rgb)

  return render_template("index.html", form=form)


if __name__ == "__main__":
  app.run(debug=True)
#Create a flask app to accept images
#A script will run and return a set of RGB values
#Create a card in html which will process the list and create a pallete