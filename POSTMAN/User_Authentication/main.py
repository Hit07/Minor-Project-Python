import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xV4#2shwnbkv#'

# flask-login to authenticate the users
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = werkzeug.security.generate_password_hash(password=password,method='pbkdf2:sha256',salt_length=8)
        if db.session.execute(db.select(User).filter(User.email == email)).scalars().all():
            flash('Email already exists!!')
            return redirect(url_for('login'))
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets', user_id=new_user.id))
    return render_template("register.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login',methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("The provided email is not registered!!")
            error = "User doesn't exist"
        elif not check_password_hash(user.password,password):
            error = 'Password Incorrect'
        elif user and check_password_hash(user.password,password):
            login_user(user=user)
            flash("You were successfully logged in!!")
            return redirect(url_for('secrets',user_id=user.id))
        else:
            error = 'Unsuccessful, Password did not match'
    return render_template("login.html",error=error)


@app.route('/secrets/<int:user_id>')
def secrets(user_id):
    user = db.get_or_404(User, user_id)
    return render_template("secrets.html", user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
def download():
    try:
        return send_from_directory(directory='static',path='files/cheat_sheet.pdf')
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
