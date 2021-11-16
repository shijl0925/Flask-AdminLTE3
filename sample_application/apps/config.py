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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    FLASK_ADMINLTE_TEXT_SM = True
    FLASK_ADMINLTE_SIDEBAR_COLLAPSE = True
    # FLASK_ADMINLTE_SIDEBAR_MINI = False
    # FLASK_ADMINLTE_MAV_LEGACY = True
    # FLASK_ADMINLTE_NAVBAR_FIXED = True
    # FLASK_ADMINLTE_FOOTER_FIXED = True
    # FLASK_ADMINLTE_DARK_MODE = True
    # FLASK_ADMINLTE_NARBAR_DARK_MODE = True


class TestingConfig(DevelopmentConfig):
    pass


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'postgresql://deploy:deploy@wz_123@localhost/analysis'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
