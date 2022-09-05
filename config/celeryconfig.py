#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 9:26
# @Author  : Arrow
# @Describe: celery配置
"""
linux:
celery启动命令 celery -A main.celery worker --loglevel=info
win10:
pip install eventlet
否则报错ValueError: not enough values to unpack (expected 3, got 0)
celery启动命令 celery -A application.celery worker --loglevel=info -P eventlet
"""

broker_url = 'redis://127.0.0.1:6379/0'
result_backend = 'redis://127.0.0.1:6379/1'