#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import os
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.menu import MenuLink


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


class MyBaseModelview(AdminLTEModelView):
    page_size = 50  # the number of entries to display on the list view

    can_export = True
    can_view_details = True

    # edit_modal = True
    # create_modal = True
    # details_modal = True


admin = Admin(name='Admin Dashboard',
              base_template='myadmin3/my_master.html',
              template_mode='bootstrap4',
              index_view=MyAdminIndexView())

admin.add_link(MenuLink(name='Back Home', class_name='nav-item', endpoint='index.index_home'))

