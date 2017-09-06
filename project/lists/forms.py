from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email
from project.users.forms import DeleteForm
from project.models import List

class ListForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])