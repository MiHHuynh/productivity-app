from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField
from wtforms.validators import DataRequired, Optional
from project.users.forms import DeleteForm
from project.models import List, ToDoItem

class ToDoItemForm(FlaskForm):
	description = StringField('Description', validators=[DataRequired()])
	due_date = DateField('Due Date', format='%m/%d/%Y', validators=[Optional()])
	is_complete = BooleanField('Completed?', validators=[Optional()])