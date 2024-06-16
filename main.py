from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
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
class User(db.Model):
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
        # Verifying new user by email
        user = db.session.execute(db.Select(User).where(User.email == register_form.email.data)).scalar()
        if user:
            flash('Account already exists!')
            return redirect(url_for('login'))

        # Verify user password if user is new
        elif register_form.password.data != register_form.confirm_password.data:
            flash('Password does not match! Confirm password before submitting.')
            return redirect(url_for('register'))

        # Proceed if password matches
        # Hash the user's password for security
        hashed_password = generate_password_hash(
            register_form.password.data,
            method="pbkdf2:sha256",
            salt_length=8,  # Salting for password
        )

        # Create User object for new user
        new_user = User(
            name=register_form.name.data,
            email=register_form.email.data,
            password=hashed_password
        )

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
