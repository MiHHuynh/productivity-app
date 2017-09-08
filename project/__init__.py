from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import os
	
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
modus = Modus(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

if os.environ.get('ENV') == 'production':
	app.config.from_object('config.ProductionConfig')
else:
	app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from project.models import User

from project.blacklistedsites.views import blacklistedsites_blueprint
from project.lists.views import lists_blueprint
from project.todoitems.views import todoitems_blueprint
from project.users.views import users_blueprint

app.register_blueprint(blacklistedsites_blueprint, url_prefix='/blacklistedsites')
app.register_blueprint(lists_blueprint, url_prefix='/users/<int:user_id>/lists')
app.register_blueprint(todoitems_blueprint, url_prefix="/users/<int:user_id>/lists/<int:list_id>/todoitems")
app.register_blueprint(users_blueprint, url_prefix='/users')

login_manager.login_view = "users.login"
login_manager.login_message = "Please log in!"

@app.route('/')
def root():
	return render_template('landingpage.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)