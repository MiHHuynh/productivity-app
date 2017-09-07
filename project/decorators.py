from flask_login import login_user, logout_user, current_user, login_required
from flask import flash, redirect, url_for
from functools import wraps
from project.models import User

def ensure_correct_user(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		correct_id = kwargs.get('user_id') or kwargs.get('id')
		if correct_id != current_user.id:
			flash("Not authorized.")
			return redirect(url_for('lists.index', user_id=current_user.id))
		return fn(*args, **kwargs)
	return wrapper


# def ensure_correct_user(fn):
# 	@wraps(fn)
# 	def wrapper(*args, **kwargs):
# 		if kwargs.get('id') != current_user.id:
# 			flash("Not authorized.")
# 			return redirect(url_for('lists.index', user_id=current_user.id))
# 		return fn(*args, **kwargs)
# 	return wrapper