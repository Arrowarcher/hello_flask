#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 20:56
# @Author  : Arrow
# @Describe:
from application import celery


@celery.task(bind=True)
def add(self, x, y):
    print(self, x + y)
    return x + y