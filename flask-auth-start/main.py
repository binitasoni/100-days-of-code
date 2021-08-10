from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=["POST","GET"])
def register():
    users = User.query.all()
    if request.method == 'POST':
        for user in users:
            if user.email==request.form.get('email'):
                flash('Email address already exists')
                return redirect(url_for('login'))
        password = request.form.get('password')
        p=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user=User(
         name=request.form.get('name'),
         email = request.form.get('email'),
         password=p
        )
        print(p)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html")


@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == 'POST':
     email = request.form.get('email')
     password = request.form.get('password')

     users=User.query.all()
     for user in users:
         print(user.password)
         if user.email==email and  check_password_hash(user.password,password):
             flash('Logged in successfully.')
             return redirect(url_for('secrets',user=user))
         if (check_password_hash(user.password,password)==False):
             flash('Please check your login details and try again.')
             return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download',methods=['GET'])
def download():
    return send_from_directory('static',
                               "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
