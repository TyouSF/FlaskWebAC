# coding: utf-8
"""
    Author: Tyou
"""

from flask import Flask

# 安装 bootstrap-flask：flask 对 bootstrap 最新版本支持的第三方扩展，基于 flask_bootstrap
from flask_bootstrap import Bootstrap

# 日期处理类库
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.confi.from_pyfile('settings.py')  # 加载配置文件
app.jinja_env.trim_blocks = True  # 删除 Jinja 模板中标签之后的空行
app.jinja_env.lstrip_blocks = True  # 删除 Jinja 模板中标签之前的空行/制表符

db = SQLAlchemy(app)  # 实例化 ORM 映射
bootstrap = Bootstrap(app)  # 实例化 Bootstrap 支持类
moment = Moment(app)  # 实例化时间处理类

from sayhello import views, commands, errors
