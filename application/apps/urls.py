#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 15:47
# @Author  : Arrow
# @Describe:
from application.utils import include

urlpatterns = [
    include("/hello", "hello.urls"),
]