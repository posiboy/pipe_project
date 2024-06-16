from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from forms import LoginForm, UploadForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
Bootstrap5(app)


# Database Initialization
# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
# ----- Table for user accounts ----- #
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(250))


with app.app_context():
    # Create any new tables (does not affect or update existing tables)
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pass
    return render_template('login.html', form=login_form)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    upload_form = UploadForm()
    if upload_form.validate_on_submit():
        pass
    return render_template('upload.html', form=upload_form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        pass
    return render_template('register.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
