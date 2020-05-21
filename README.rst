====================
Flask-AdminLTE3
====================

Flask-AdminLTE3 packages `AdminLTE3
<http://www.almsaeedstudio.com/>`_ into an extension that mostly consists
of a blueprint named 'adminlte'. It can also create links to serve AdminLTE and works with no boilerplate code in your application.

Installation
============

Install::

    pip install Flask-AdminLTE3


Compatibility
-------------

This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.


Usage
=====



Here is an example::

  from flask_adminlte import AdminLTE

  [...]

  AdminLTE()(app)


  from flask_adminlte import AdminLTEModelView, AdminLTEFileAdmin
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


myadmin/my_master.html::
  {% extends 'adminlte3/base.html' %}
  [...]

myadmin/my_index.html::
  {% extends 'adminlte3/my_master.html' %}
  {% block body %}
  {{ super() }}
  [...]
  {% endblock body %}


This makes some new templates available, containing blank pages that include all
bootstrap resources, and have predefined blocks where you can put your content.