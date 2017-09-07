from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets, PasswordField
from wtforms.validators import DataRequired, Email
from project.models import User

class UserForm(FlaskForm):
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

class DeleteForm(FlaskForm):
	pass