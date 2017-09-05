from flask import redirect, render_template, request, url_for, Blueprint
# from project.users.forms import UserForm
from project.models import User
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/')
def index():
	pass
	# probably should only be visible to an admin to view all users

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
	# GET renders signup form
	# POST will sign user up and redirect to welcome
	return render_template('users/signup.html')

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	# GET renders login form
	# POST will sign user in and redirect to welcome
	pass

@users_blueprint.route('/welcome')
def welcome():
	pass
	# render DASHBOARD
	# dashboard would be...

@users_blueprint.route('/<int:user_id>/show')
def show(user_id):
	# PATCH
	# edit account details
	# DELETE
	# delete account
	# GET
	# show account details
	pass

@users_blueprint.route('/<int:user_id>/edit')
def edit(user_id):
	pass
	# render edit form, like edit account details
