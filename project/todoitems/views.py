from flask import Blueprint
from project import db

todoitems_blueprint = Blueprint('todoitems', __name__, template_folder='templates')