# Flask-AdminLTE3


Flask-AdminLTE3 packages [AdminLTE3](https://adminlte.io/themes/dev/AdminLTE/index.html) into an extension that mostly consists
of a blueprint named 'adminlte'. It is Admin Theme for Flask-Admin.

## Installation

Installation using pip:

    pip install Flask-AdminLTE3
    

## Compatibility

This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.

## Usage

Here is an example:

    from flask_adminlte3 import AdminLTE3
    
    [...]
    
    AdminLTE3(app)


## Admin Theme for Flask-Admin

    from flask_admin.contrib.sqla import ModelView
    from flask_admin.contrib.fileadmin import FileAdmin


    class AdminLTEModelView(ModelView):
        list_template = 'flask-admin/model/list.html'
        create_template = 'flask-admin/model/create.html'
        edit_template = 'flask-admin/model/edit.html'
        details_template = 'flask-admin/model/details.html'

        create_modal_template = 'flask-admin/model/modals/create.html'
        edit_modal_template = 'flask-admin/model/modals/edit.html'
        details_modal_template = 'flask-admin/model/modals/details.html'


    class AdminLTEFileAdmin(FileAdmin):
        list_template = 'flask-admin/file/list.html'

        upload_template = 'flask-admin/file/form.html'
        mkdir_template = 'flask-admin/file/form.html'
        rename_template = 'flask-admin/file/form.html'
        edit_template = 'flask-admin/file/form.html'

        upload_modal_template = 'flask-admin/file/modals/form.html'
        mkdir_modal_template = 'flask-admin/file/modals/form.html'
        rename_modal_template = 'flask-admin/file/modals/form.html'
        edit_modal_template = 'flask-admin/file/modals/form.html'


    class MyAdminIndexView(AdminIndexView):
        @expose('/', methods=['GET', 'POST'])
        def index(self):
            return self.render('myadmin3/my_index.html')


    from flask_admin import Admin
    admin = Admin(name='Admin Dashboard',
                base_template='myadmin3/my_master.html',
                template_mode='bootstrap4',
                index_view=MyAdminIndexView())


base template myadmin3/my_master.html code:

    {% extends 'flask-admin/base.html' %}
    [...]

index template myadmin3/my_index.html code:

    {% extends 'myadmin3/my_master.html' %}
    [...]
    
## Screenshots

Admin Area:

* Demo Model :![model screenshot](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/demo-admin-home.png)

* Demo List Model: ![model list](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/demo-admin-list.png)

* Demo Creating Model: ![model create](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/demo-admin-create.png)

* Demo Editing Model: ![model edit](https://raw.githubusercontent.com/shijl0925/Flask-AdminLTE3/master/screenshots/demo-admin-edit.png)