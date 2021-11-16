import os
from flask import Flask
from apps.extensions import adminlte
from apps.controller.admin import admin
from apps.views import init_blue_print
from apps.config import config


def create_app(env=None):
    app_ = Flask(__name__)
    if env is None:
        env = os.environ.get('FLASK_ENV', 'default')
    app_.config.from_object(config.get(env))
    admin.init_app(app_)
    adminlte.init_app(app_)
    init_blue_print(app_)
    return app_


app = create_app()




