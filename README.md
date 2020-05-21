AdminLTE3 Templates, Template Tags, and Admin Theme for Flask-Admin
=============================================================

Flask-AdminLTE3 packages `AdminLTE3
<http://www.almsaeedstudio.com/>`_ into an extension that mostly consists
of a blueprint named 'adminlte'. It can also create links to serve AdminLTE3 and works with no boilerplate code in your application.

Installation
------------

Installation using pip:

    pip install Flask-AdminLTE3

Compatibility
-------------

This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.

Usage
-----
Here is an example:

    from flask_adminlte3 import AdminLTE3
    
    [...]
    
    AdminLTE3()(app)


    from flask_adminlte3 import AdminLTEModelView, AdminLTEFileAdmin
    class MyModelView(AdminLTEModelView):
        pass

    class MyFileAdmin(AdminLTEFileAdmin):
        pass

    class MyAdminIndexView(AdminIndexView):
        @expose('/', methods=['GET', 'POST'])
        def index(self):
            return self.render('myadmin/my_index.html')

    from flask_admin import Admin
    admin = Admin(name='Admin Dashboard',
                base_template='myadmin/my_master.html',
                template_mode='bootstrap4',
                index_view=MyAdminIndexView())


base template myadmin/my_master.html code:

    {% extends 'adminlte3/base.html' %}
    [...]

index template myadmin/my_index.html code:

    {% extends 'adminlte3/my_master.html' %}
    {% block body %}
    {{ super() }}
    [...]
    {% endblock body %}


This makes some new templates available, containing blank pages that include all
bootstrap resources, and have predefined blocks where you can put your content.

Screenshots
-----------
Admin Area:
    
* Home :![admin screenshot](https://github.com/shijl0925/Flask-AdminLTE3/blob/master/screenshots/home.png)

* Demo Model :![model screenshot](https://github.com/shijl0925/Flask-AdminLTE3/blob/master/screenshots/demo-home.png)

* Demo List Model: ![model list](https://github.com/shijl0925/Flask-AdminLTE3/blob/master/screenshots/demo-list.png)

* Demo Creating Model: ![model create](https://github.com/shijl0925/Flask-AdminLTE3/blob/master/screenshots/demo-create.png)

* Demo Editing Model: ![model edit](https://github.com/shijl0925/Flask-AdminLTE3/blob/master/screenshots/demo-edit.png)
