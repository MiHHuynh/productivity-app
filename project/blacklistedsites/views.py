from flask import Blueprint
from project import db

blacklistedsites_blueprint = Blueprint('blacklistedsites', __name__, template_folder='templates')