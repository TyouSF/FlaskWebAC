# coding: utf-8
"""
    Author: Tyou
"""

import os
import sys
from sayhello import app

# 根据系统判定 sqlite 本地连接符前缀
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# SQLite 本项目根目录下数据库文件的地址
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')  # 配置安全密钥
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)  # 获取数据库连接地址
