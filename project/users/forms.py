from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets, PasswordField
from wtforms.validators import DataRequired, Email
from project.models import User

class UserForm(FlaskForm):
	email = StringField('email', validators=[DataRequired(), Email()])
	password = StringField('password', validators=[DataRequired()])

class DeleteUserForm(FlaskForm):
	pass