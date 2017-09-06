from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.models import User, List, ToDoItem
from project.todoitems.forms import ToDoItemForm, DeleteForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError

todoitems_blueprint = Blueprint('todoitems', __name__, template_folder='templates')

@todoitems_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id, list_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	if request.method == 'POST':
		form = ToDoItemForm(request.form)
		if form.validate():
			new_todoitem = ToDoItem(form.data['description'], form.data['due_date'], found_list.id)
			db.session.add(new_todoitem)
			db.session.commit()
			flash("You have successfully created a new to-do item!")
			return redirect(url_for('todoitems.index', user_id=user.id, list_id=found_list.id))
		flash("Something went wrong in creating a new item. Please try again.")
		return redirect(url_for('todoitems.new', user_id=user.id, list_id=found_list.id))
	return render_template('todoitems/index.html', user=user, found_list=found_list)

@todoitems_blueprint.route('/new')
def new(user_id, list_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	form = ToDoItemForm()
	return render_template('todoitems/new.html', form=form, user=user, found_list=found_list)

@todoitems_blueprint.route('/<int:item_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, list_id, item_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	todoitem = ToDoItem.query.get(item_id)
	pass

@todoitems_blueprint.route('/<int:item_id>/edit')
def edit(user_id, list_id, item_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	todoitem = ToDoItem.query.get(item_id)
	pass
