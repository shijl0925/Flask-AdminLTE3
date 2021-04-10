__version__ = '1.0.8'
from flask import Blueprint


class AdminLTE3(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['adminlte'] = self

        blueprint = Blueprint('adminlte',
                              __name__,
                              template_folder='templates',
                              static_folder='static',
                              static_url_path=app.static_url_path + '/adminlte')

        app.register_blueprint(blueprint)
