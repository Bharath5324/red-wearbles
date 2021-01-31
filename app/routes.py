from api import API_APP
from webapp import WEBAPP
def init_app(app):
    app.register_blueprint(WEBAPP, url_prefix='/')
    app.register_blueprint(API_APP, url_prefix='/user')