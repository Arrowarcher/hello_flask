#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 14:38
# @Author  : Arrow
# @Describe:
import os
import click
from app import app


def register_public_command(app):
    @app.cli.command("hello")
    @click.argument("name")
    @click.argument("qwq")
    def hello(name, qwq):
        print("name=%s\nqwq=%s" % (name, qwq))
        print("命令执行了！！！")

    @app.cli.command("startapp")
    @click.argument("startapp")
    def hello(startapp):
        startapp = f"apps/{startapp}"
        if startapp is None:
            print('文件名不能为空！')
            return
        elif not os.path.isdir(startapp):
            os.mkdir(startapp)
            open("%s/views.py" % startapp, 'w')
            open("%s/models.py" % startapp, 'w')
            open("%s/__init__.py" % startapp, 'w')
            with open("%s/urls.py" % startapp, 'w') as f:
                f.write("""from . import views
    urlpatterns = [

    ]
    """)
            print('创建成功！')
        else:
            print("创建失败！文件名已存在")
