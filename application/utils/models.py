#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 19:02
# @Author  : Arrow
# @Describe:
from application import db
from datetime import datetime


class BaseModel(db.Model):
    """公共模型"""
    __abstract__ = True     # 抽象模型
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    is_deleted = db.Column(db.Boolean, default=False, comment="逻辑删除")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.id)