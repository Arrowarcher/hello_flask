# hello_flask

模仿dj模块化

### 蓝图模块在application/apps里写

urls.py 是总路由
hello/urls.py 模块路由
hello/models.py orm表
hello/views.py 视图函数
hello/tasks.py celery异步任务

### config目录
配置目录


### 待引入优化
1. migrate模块，每次数据库迁移记录，方便增加新功能
2. Marshmallow 相当于drf的序列化模块
3. 应用程序错误处理，增加json错误码返回
4. 引入Flask appbuilder或者flask-admin作为后台模块，或者它们的接口快速生成curd功能
