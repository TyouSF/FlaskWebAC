#  coding: utf=8
"""
    Author: Tyou
"""

from flask import render_template
from sayhello import app


# 捕获系统 404 错粗，并给出页面提示
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 捕获系统 500 错误，并给出页面提示
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
