#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 20:41
# @Author  : Arrow
# @Describe: celery初始化
from celery import Celery

celery = Celery("flask")
celery.config_from_object('config.celeryconfig')
celery.autodiscover_tasks(celery)

def register_celery(app):

    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask