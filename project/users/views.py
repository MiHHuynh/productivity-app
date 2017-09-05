from flask import Blueprint
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='templates')