from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.models import User, List
from project.lists.forms import ListForm, DeleteForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from functools import wraps
from project.decorators import ensure_correct_user
from flask_login import login_user, logout_user, current_user, login_required

lists_blueprint = Blueprint('lists', __name__, template_folder='templates')

@lists_blueprint.route('/', methods=['GET', 'POST'])
# @login_required
# @ensure_correct_user
def index(user_id):
	user = User.query.get(user_id)
	form = ListForm(request.form)
	if request.method == 'POST':
		if form.validate():
			new_list = List(form.data['name'], user.id)
			db.session.add(new_list)
			db.session.commit()
			flash("You have successfully created a new list!")
			return redirect(url_for('lists.index', user_id=user.id))
		flash("Something went wrong in creating a new list. Please try again.")
		return redirect(url_for('lists.new'))
	return render_template('lists/index.html', user=user)

@lists_blueprint.route('/new')
# @login_required
# @ensure_correct_user
def new(user_id):
	form = ListForm(request.form)
	user = User.query.get(user_id)
	return render_template('lists/new.html', user=user, form=form)

@lists_blueprint.route('/<int:list_id>', methods=['GET', 'PATCH', 'DELETE'])
# @login_required
# @ensure_correct_user
def show(user_id, list_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	if request.method == b'PATCH':
		form = ListForm(request.form)
		if form.validate():
			found_list.name = form.data['name']
			db.session.add(found_list)
			db.session.commit()
			flash("You have successfully edited your list!")
			return redirect(url_for('lists.show', user_id=user.id, list_id=found_list.id))
		else:
			flash("Something went wrong in editing your list. Please try again.")
			return redirect(url_for('lists.edit', user_id=user.id, list_id=found_list.id))
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_list)
			db.session.commit()
			flash("You have successfully deleted your list!")
			return redirect(url_for('lists.index', user_id=user.id))
		else:
			flash("Something went wrong in deleting your list. Pleast try again.")
			return redirect(url_for('lists.edit', user_id=user.id, list_id=found_list.id))
	return render_template('lists/show.html', user=user, found_list=found_list)

@lists_blueprint.route('/<int:list_id>/edit')
# @login_required
# @ensure_correct_user
def edit(user_id, list_id):
	user = User.query.get(user_id)
	found_list = List.query.get(list_id)
	form = ListForm(obj=found_list)
	delete_form = DeleteForm(obj=found_list)
	return render_template('lists/edit.html', user=user, found_list=found_list, form=form, delete_form=delete_form)