from flask import Blueprint
from project import db

lists_blueprint = Blueprint('lists', __name__, template_folder='templates')