#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import flask

index_bp = flask.Blueprint('index', __name__, url_prefix='/')


@index_bp.route('/', methods=['GET'])
def index_home():
    return flask.redirect(flask.url_for("admin.index"))

