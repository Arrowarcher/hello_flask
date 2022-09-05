#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 16:59
# @Author  : Arrow
# @Describe: 顶层配置，项目中可直接导入，不需要app上下文

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    "hello"
]