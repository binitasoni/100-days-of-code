from flask import Flask, render_template
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import validators, ValidationError
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key="bini"
Bootstrap(app)
class MyForm(FlaskForm):
    email = StringField('name',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField("LogIn")
@app.route("/")
def home():
    form = MyForm()
    return render_template('index.html',form=form)
@app.route("/login",methods=["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit() and form.email.data=="admin@email.com" and form.password.data=="12345678":
        return render_template('success.html')
    else:
        return render_template('denied.html')

    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)