#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 16:30
# @Author  : Arrow
# @Describe:
# 导入基础配置（可覆盖）
from config.base_settings import *


# DEBUG调试模式
DEBUG = True
ENV = "development"
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = True


# 导入顶层配置（不可改）
from config.settings import *

