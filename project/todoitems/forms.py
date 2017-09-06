from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Optional
from project.users.forms import DeleteForm
from project.models import List, ToDoItem

class ToDoItemForm(FlaskForm):
	description = StringField('Name', validators=[DataRequired()])
	due_date = DateField('Due Date', format='%m/%d/%Y', validators=[Optional()])