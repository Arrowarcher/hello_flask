#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 16:16
# @Author  : Arrow
# @Describe:
from flask import Flask

from application.modules.celery import register_celery, celery
from config.settings import BASE_DIR
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_file="config/dev_cfg.py"):
    print(__name__, config_file, BASE_DIR)
    app = Flask(__name__, root_path=BASE_DIR)
    # 从配置文件加载配置
    app.config.from_pyfile(config_file)

    # 初始化db
    db.app = app
    db.init_app(app)
    # 注册celey
    register_celery(celery, app)

    # 注册蓝图
    # from application.apps.hello import hello as hello_buleprint
    # app.register_blueprint(hello_buleprint)
    from application.utils import init_blueprint
    init_blueprint(app)

    print(f"app_url_map:{app.url_map}")

    if app.debug:
        # shell变量增加，方便调试
        @app.shell_context_processor
        def make_shell_context():
            return dict(db=db)

    return app

