#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 15:25
# @Author  : Arrow
# @Describe:
from flask import Blueprint
from importlib import import_module

from flask_restful import Api
from werkzeug.utils import import_string

from application.apps import local_path as apps_path, total_url_path


def path(rule, func_view, **kwargs):
    # 把蓝图下视图和路由之间的映射关系处理成字典结构，方便后面注册蓝图的时候，直接传参
    return {"rule": rule, "view_func": func_view, **kwargs}


def resource_path(resource, *urls, **kwargs):
    # 把视图和路由之间的映射关系处理成字典结构，方便后面注册flask_restful_api的时候，直接传参
    return {"resource": resource, "urls": urls, **kwargs}


def include(url_prefix, blueprint_path):
    """把路由前缀和蓝图进行关系映射"""
    return {"url_prefix": url_prefix, "blueprint_path": blueprint_path}


def init_blueprint(app):
    """自动注册蓝图"""
    # 读取总路由文件
    urlpatterns = import_string(f"{total_url_path}.urlpatterns")
    # 构造映射字典
    url_prefix_map = {}
    for urlpattern in urlpatterns:
        # {"hello.urls": url_prefix}
        url_prefix_map[urlpattern["blueprint_path"]] = urlpattern["url_prefix"]

    installed_apps = app.config.get("INSTALLED_APPS")
    for blueprint_path in installed_apps:
        if "." not in blueprint_path:
            blueprint_name = blueprint_path
            blueprint_path = apps_path + '.' + blueprint_name
        else:
            blueprint_name = blueprint_path.split(".")[-1]

        try:
            urlpatterns = import_string(f"{blueprint_path}.urls.urlpatterns")
        except ImportError as e:
            pass
        else:
            url_prefix = url_prefix_map.get(f"{blueprint_name}.urls", f"/{blueprint_name}")
            # 自动创建蓝图对象
            blueprint = Blueprint(name=blueprint_name, import_name=blueprint_path, url_prefix=url_prefix)

            # 创建API对象
            api = Api(blueprint)

            # 蓝图或flask_restful自动绑定视图和子路由
            for url_dict in urlpatterns:  # 遍历子路由中的所有路由关系
                # blueprint.add_url_rule(**url)  # 注册到蓝图下
                urls = url_dict.pop("urls")
                resource = url_dict.pop("resource")
                api.add_resource(resource, *urls, **url_dict)

            # 注册蓝图对象到app应用对象中
            app.register_blueprint(blueprint)

        # 注册模型
        try:
            import_string(blueprint_path + ".models")
        except:
            pass
        # 加载蓝图内部的admin站点配置
        try:
            import_string(blueprint_path + ".admin")
        except:
            pass

        # 加载蓝图内部的socket接口
        try:
            import_string(blueprint_path + ".socket")
        except:
            pass

