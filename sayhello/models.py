# coding: utf-8
"""
    Author: Tyou
"""

from datetime import datetime
from sayhello import db


# 消息模型类（可以实例化为对应的数据库）
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
