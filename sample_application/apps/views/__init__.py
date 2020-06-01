#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from .index import index_bp

bps = [index_bp]


def init_blue_print(app):
    for bp in bps:
        app.register_blueprint(bp)
