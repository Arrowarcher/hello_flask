import os

from flask import Blueprint
from flask_restful import Api

from application.modules.logger import get_logger
from config.settings import BASE_DIR

LOG_FILE = os.path.join(BASE_DIR, "log", f"{__name__}.log")
LOG_LEVEL = "INFO"
logger = get_logger(__name__, LOG_FILE, log_level=LOG_LEVEL)


# 实例化蓝本对象，必须指定name蓝本名字，import_name蓝本所在包或模块
hello = Blueprint(name='hello', import_name=__name__, url_prefix='/hello')

api = Api(hello)

# 配置views路由
from . import views
api.add_resource(views.AuthorAPI, "/authors/<author_id>", endpoint="author")
api.add_resource(views.AuthorListAPI, "/authors", endpoint="authorList")
