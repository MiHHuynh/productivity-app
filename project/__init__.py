from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
modus = Modus(app)
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/productivity-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

from project.blacklistedsites.views import blacklistedsites_blueprint
from project.lists.views import lists_blueprint
from project.todoitems.views import todoitems_blueprint
from project.users.views import users_blueprint

# REMOVE AFTER MORE CODE IS WRITTEN. ADDED TO TRIGGER DB MIGRATIONS
import project.models

app.register_blueprint(blacklistedsites_blueprint, url_prefix='/blacklistedsites')
app.register_blueprint(lists_blueprint, url_prefix='/lists')
app.register_blueprint(todoitems_blueprint, url_prefix="/todoitems")
app.register_blueprint(users_blueprint, url_prefix='/users')

@app.route('/')
def root():
	return "HELLO!"