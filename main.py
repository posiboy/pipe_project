from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pass
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
