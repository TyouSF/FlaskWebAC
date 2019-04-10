# 个人博客

**目录/文件详解**

| 文件/路径                                            | 说明                       |
| :----------------------------------------------- | :----------------------- |
| [test_hello.py](test_sayhello.py)                | 基于 Unittest 实现的单元测试      |
| [.flaskenv](.flaskenv)                           | 变量配置文件，指定 FLASK_APP 等    |
| [sayhello/\_\_init\_\_.py](sayhello/__init__.py) | 项目已包的形式组装，核心 app，db 等写于此 |
| [sayhello/commands.py](sayhello/commands.py)     | 总定义的初始化命令                |
| [sayhello/errors.py](sayhello/errors.py)         | 自定义处理错误页面                |
| [sayhello/models.py](sayhello/models.py)         | 留言板模型数据                  |
| [sayhello/forms.py](sayhello/forms.py)           | 渲染表单的 WTForms 类          |
| [sayhello/views.py](sayhello/views.py)           | 主视图                      |
| [sayhello/settings.py](sayhello/settings.py)     | 配置参数：如数据库连接地址等           |
