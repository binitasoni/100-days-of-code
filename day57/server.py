from flask import Flask
from flask import render_template
import requests
def gender(name):
    endpoint=f"https://api.genderize.io?name={name}"
    response = requests.get(url=endpoint)
    data = response.json()
    return data['gender']
def age(name):
    endpoint=f"https://api.agify.io?name={name}"
    response = requests.get(url=endpoint)
    data = response.json()
    return data['age']
app=Flask(__name__)
import datetime
@app.route("/")
def home():
     year=datetime.date.today().year
     return render_template('index.html',year=year)
@app.route("/guess/<name>")
def guess(name):
    age_person=age(name)
    gender_person=gender(name)
    return render_template('guess.html', age=age_person,gender=gender_person,name=name)
@app.route("/blog")
def blog():
    endpoint = f"https://api.npoint.io/82975389c85afb34e389"
    response = requests.get(url=endpoint)
    blogs = response.json()
    return render_template('blog.html',blogs=blogs)
if __name__ == '__main__':
    app.run(debug=True)