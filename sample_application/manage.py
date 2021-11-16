#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from flask_script import Manager
from apps import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
