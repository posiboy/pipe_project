from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


# class UploadForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
#     location = StringField('Location', validators=[DataRequired(), Length(min=2, max=100)])
#     rating = IntegerField('Rating', validators=[DataRequired()])
#     content = TextAreaField('Content', validators=[DataRequired()])
#     picture = FileField('Update Picture', validators=[FileAllowed(['jpg', 'png'])])
#     submit = SubmitField('Post')
