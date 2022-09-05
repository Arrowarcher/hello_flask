#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/29 15:11
# @Author  : arrow
# @Describe    :

from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from .models import Author, db

#  reqparse.RequestParser()
# 定义请求进来的参数，可以解析、校验参数
get_parser = reqparse.RequestParser()
get_parser.add_argument('test_id', location='args', type=str)
get_parser.add_argument('name', location='args', type=str)

post_parser = reqparse.RequestParser()
# location=('json', 'values',)默认
post_parser.add_argument('name', type=str, required=True, help="name is required")


test_list_parser = reqparse.RequestParser()
test_list_parser.add_argument('page', location='args', type=int)
test_list_parser.add_argument('per_page', location='args', type=int)
test_list_parser.add_argument('search', location='args', type=str)


# 格式化输出
resource_full_fields = {
    'id': fields.Integer,
    'name': fields.String
}
# fields.Nested可嵌套
page_resource_fields = {
    "total": fields.Integer,
    'items': fields.Nested(resource_full_fields)
}


class AuthorAPI(Resource):

    @marshal_with(resource_full_fields)
    def get(self, author_id=None):
        params = get_parser.parse_args()
        name = params.get('name')
        if author_id:
            test = db.session.query(Author).filter_by(id=author_id).first()
            # test = Author.query.filter_by(id=author_id).first()
            if test:
                return test
            else:
                # 加上marshal_with后会返回{
                #     "data": {
                #         "id": 0,
                #         "name": null
                #     }
                # }，而不是返回这里写的东西
                return {"code": 200, "message": "article no exists"}
        elif name:
            # test = Author.query.filter_by(name == name).first()
            test = db.session.query(Author).filter(Author.name == name).first()
            if test:
                return test
            else:
                test = db.session.query(Author).filter(Author.name.like(f"%{name}%")).first()
                if test:
                    return test
                return {"code": 200, "message": "test no exists"}
        else:
            return {"code": 404, "message": "test no exists"}


class AuthorListAPI(Resource):
    @marshal_with(page_resource_fields)
    def get(self):
        params = test_list_parser.parse_args()
        page = params.get('page')
        per_page = params.get('per_page')
        search = params.get('search')
        test_query = db.session.query(Author)
        if search:
            test_query = test_query.filter(Author.name.like(f"%{search}%"))
        test_query = test_query.paginate(page, per_page)
        return test_query

    @marshal_with(resource_full_fields)
    def post(self):
        params = post_parser.parse_args()
        new_obj = Author(**params)
        db.session.add(new_obj)
        db.session.commit()
        return new_obj