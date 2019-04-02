# coding: utf-8
"""
    Author: Tyou
"""

from flask import flash, render_template, redirect, url_for

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('信息已成功发送')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
