from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin


class AdminLTE3(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        blueprint = Blueprint('adminlte',
                              __name__,
                              template_folder='templates',
                              static_folder='static',
                              static_url_path=app.static_url_path + '/adminlte')

        app.register_blueprint(blueprint)

        app.extensions['adminlte'] = self


class AdminLTEModelView(ModelView):
    list_template = 'adminlte3/model/list.html'
    create_template = 'adminlte3/model/create.html'
    edit_template = 'adminlte3/model/edit.html'
    details_template = 'adminlte3/model/details.html'

    create_modal_template = 'adminlte3/model/modals/create.html'
    edit_modal_template = 'adminlte3/model/modals/edit.html'
    details_modal_template = 'adminlte3/model/modals/details.html'


class AdminLTEFileAdmin(FileAdmin):
    list_template = 'adminlte3/file/list.html'

    upload_template = 'adminlte3/file/form.html'
    mkdir_template = 'adminlte3/file/form.html'
    rename_template = 'adminlte3/file/form.html'
    edit_template = 'adminlte3/file/form.html'

    upload_modal_template = 'adminlte3/file/modals/form.html'
    mkdir_modal_template = 'adminlte3/file/modals/form.html'
    rename_modal_template = 'adminlte3/file/modals/form.html'
    edit_modal_template = 'adminlte3/file/modals/form.html'