from flask import Blueprint
API_APP = Blueprint(__name__, 'api', template_folder='templates')

from . import routes