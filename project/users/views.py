from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.models import User
from project.users.forms import UserForm, DeleteForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError

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
			except IntegrityError as e:
				return render_template('signup.html', form=form)
			flash("You have successfully created an account!")
			return redirect(url_for('users.welcome'))
	return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			found_user = User.query.filter_by(email=form.data['email'].first())
			if found_user:
				authenticated_user = bcrypt.check_password_has(found_user.password, form.data['password'])
				if authenticated_user:
					flash("Welcome back!")
					return redirect(url_for('users.welcome'))
		flash("Please log in.")
		return redirect(url_for('users.login'))
	return render_template('users/login.html', form=form)

@users_blueprint.route('/welcome')
def welcome():
	return render_template('users/welcome.html')
	# return redirect(url_for('lists.index'))
	# render DASHBOARD
	# dashboard would be...

@users_blueprint.route('/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id):
	user = User.query.get(user_id)
	delete_form = DeleteForm(request.form)
	form = UserForm(request.form)
	if request.method == b'PATCH':
		if form.validate():
			user.email = form.data['email']
			user.password = bcrypt.generate_password_hash(form.data['password']).decode('UTF-8')
			db.session.add(user)
			db.session.commit()
			flash("You have successfully changed your account details!")
			return redirect(url_for('users.show', user_id=user.id))
		else:
			flash("Something went wrong in editing your account details. Please try again.")
			return render_template('users/edit.html', user=user, form=form, delete_form=delete_form)
	if request.method == b'DELETE':
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			flash("You have successfully deleted your account.")
			return redirect(url_for('users.index'))
		else:
			flash("Something went wrong in deleting your account. Please try again.")
			return redirect(url_for('users.edit', user_id=user.id))
	return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:user_id>/edit')
def edit(user_id):
	user = User.query.get(user_id)
	form = UserForm(obj=user)
	delete_form = DeleteForm()
	return render_template('users/edit.html', user=user, form=form, delete_form=delete_form)
