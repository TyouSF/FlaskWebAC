# coding: utf-8
"""
    Author
"""

import unittest
from flask import abort
from sayhello import app, db
from sayhello.models import Message
from sayhello.commands import initdb, forge


class SayHelloTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        db.create_all()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn('404 Error', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        # create route to abort the request with the 500 Error
        @app.route('/500')
        def internal_server_error_for_test():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn('500 Error', data)
        self.assertIn('Go Back', data)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Say Hello', data)

    def test_create_message(self):
        response = self.client.post('/', data=dict(
            name='Peter',
            body='Hello, world.'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('信息已成功发送', data)
        self.assertIn('Hello, world.', data)

    def test_form_validation(self):
        response = self.client.post('/', data=dict(
            name=' ',
            body='Hello, world.'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

    def test_forge_command(self):
        result = self.runner.invoke(forge)
        self.assertIn('测试数据已生成完毕，总计 20 条', result.output)
        self.assertEqual(Message.query.count(), 20)

    def test_forge_command_with_count(self):
        result = self.runner.invoke(forge, ['--count', '50'])
        self.assertIn('测试数据已生成完毕，总计 50 条', result.output)
        self.assertEqual(Message.query.count(), 50)

    def test_initdb_command(self):
        result = self.runner.invoke(initdb)
        self.assertIn('数据已创建/初始化完毕', result.output)

    def test_initdb_command_with_drop(self):
        result = self.runner.invoke(initdb, ['--drop'], input='y\n')
        self.assertIn(
            '本操作将执行删除数据库，请确认是否继续', result.output)
        self.assertIn('数据库已删除完毕', result.output)


if __name__ == '__main__':
    unittest.main()
