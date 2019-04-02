# codinf: utf-8
"""
    Author: Tyou
"""

# 引入表单渲染类
from flask_wtf import FlaskForm
# 引入表单字段类
from wtforms import StringField, SubmitField, TextAreaField
# 引入内置数据校验器
from wtforms.validators import DataRequired, Length


# 前端页面渲染表单类
class HelloForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[
                         DataRequired(), Length(1, 200)])
    Submit = SubmitField()
