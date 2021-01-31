from flask import Blueprint
WEBAPP = Blueprint(__name__, 'webapp', template_folder='templates')

from . import routes