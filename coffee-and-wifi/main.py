from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from csv import writer
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps(URL', validators=[DataRequired()])
    cafe_open = StringField('Cafe Opening Time eg 8AM', validators=[DataRequired()])
    cafe_close = StringField('Cafe Closing Time eg 8AM', validators=[DataRequired()])
    cafe_coffee_rating = StringField('Coffee Rating', validators=[DataRequired()])
    cafe_wifi_rating = StringField('Wifi Rating', validators=[DataRequired()])
    cafe_power_rating = StringField('Power Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

from wtforms.validators import ValidationError

def _required(CafeForm, field):
    if not field.raw_data or not field.raw_data[0]:
        raise ValidationError('Field is required')
# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    name = form.cafe.data
    location = form.cafe_location.data
    open = form.cafe_open.data
    close = form.cafe_close.data
    coffee_rating = form.cafe_coffee_rating.data
    wifi_rating = form.cafe_wifi_rating.data
    power_rating = form.cafe_power_rating.data
    if form.validate_on_submit():

        List=[name,location,open,close,coffee_rating,wifi_rating,power_rating]

        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{name},"
                           f"{location},"
                           f"{open},"
                           f"{close},"
                           f"{coffee_rating},"
                           f"{wifi_rating},"
                           f"{power_rating}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows,l=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
