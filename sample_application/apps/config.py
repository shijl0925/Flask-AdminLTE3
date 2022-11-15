#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]flask_app/'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # FLASK_ADMINLTE_NAV_LEGACY = True

    # Options from
    # https://adminlte.io/docs/3.2/layout.html#layout-options
    FLASK_ADMINLTE_LAYOUT_OPTIONS = [
        "control-sidebar-slide-open",
        "sidebar-mini",  # FLASK_ADMINLTE_SIDEBAR_MINI = True
        "layout-fixed",  # FLASK_ADMINLTE_SIDEBAR_FIXED = True
        "text-sm",  # FLASK_ADMINLTE_TEXT_SM = True
        # "sidebar-collapse",  # FLASK_ADMINLTE_SIDEBAR_COLLAPSE = True
        # "dark-mode",  # FLASK_ADMINLTE_DARK_MODE = True
        "layout-navbar-fixed",  # FLASK_ADMINLTE_NAVBAR_FIXED = True
        "layout-footer-fixed",  # FLASK_ADMINLTE_FOOTER_FIXED = True
        # "layout-top-nav",
    ]

    FLASK_ADMINLTE_NAVBAR_OPTIONS = [
        "main-header",
        "navbar",
        "navbar-expand",
        "navbar-dark",
        # "navbar-white",
        # "navbar-light",
    ]


class TestingConfig(DevelopmentConfig):
    pass


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://deploy:deploy@wz_123@localhost/analysis"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
