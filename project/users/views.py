from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.models import User
from project.users.forms import UserForm, DeleteForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from functools import wraps
from project.decorators import ensure_correct_user
from flask_login import login_user, logout_user, current_user, login_required

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/')
def index():
	# probably should only be visible to an admin to view all users
	return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			try:
				new_user = User(form.data['email'], form.data['password'])
				db.session.add(new_user)
				db.session.commit()
				login_user(new_user)
			except IntegrityError as e:
				flash("That e-mail address is already taken.")
				return render_template('signup.html', form=form)
			flash("You have successfully created an account!")
			return redirect(url_for('users.welcome'))
	return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			found_user = User.query.filter_by(email=form.data['email']).first()
			if found_user:
				authenticated_user = bcrypt.check_password_hash(found_user.password, form.data['password'])
				if authenticated_user:
					login_user(found_user)
					flash("Welcome back!")
					return redirect(url_for('users.welcome'))
		flash("Please log in.")
		return redirect(url_for('users.login'))
	return render_template('users/login.html', form=form)

@users_blueprint.route('/welcome')
@login_required
def welcome():
	return redirect(url_for('lists.index', user_id=current_user.id))
	# return redirect(url_for('lists.index'))
	# render DASHBOARD
	# dashboard would be...

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
	user = User.query.get(id)
	delete_form = DeleteForm(request.form)
	form = UserForm(request.form)
	if request.method == b'PATCH':
		if form.validate():
			user.email = form.data['email']
			user.password = bcrypt.generate_password_hash(form.data['password']).decode('UTF-8')
			db.session.add(user)
			db.session.commit()
			flash("You have successfully changed your account details!")
			return redirect(url_for('lists.index', user_id=user.id))
		else:
			flash("Something went wrong in editing your account details. Please try again.")
			return render_template('users/edit.html', user=user, form=form, delete_form=delete_form)
	if request.method == b'DELETE':
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			flash("You have successfully deleted your account.")
			logout_user()
			return redirect(url_for('users.index'))
		else:
			flash("Something went wrong in deleting your account. Please try again.")
			return redirect(url_for('users.edit', id=user.id))
	return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	delete_form = DeleteForm()
	return render_template('users/edit.html', user=user, form=form, delete_form=delete_form)

@users_blueprint.route('/logout')
@login_required
def logout():
    flash("Logged out!")
    logout_user()
    return redirect(url_for('users.login'))