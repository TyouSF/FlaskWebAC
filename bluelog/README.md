# 个人博客

**目录/文件详解**

| 文件/路径                                                      | 说明                    |
| :--------------------------------------------------------- | :-------------------- |
| [\_\_init\_\_.py](bluelog/__init__.py)                     | 主程序（主要包含工厂主函数等）       |
| [emails.py](bluelog/emails.py)                             | 电子邮件处理模块              |
| [extensions.py](bluelog/extensions.py)                     | 扩展模块（如db、moment等实例化类） |
| [fakes.py](bluelog/fakes.py)                               | 虚拟数据                  |
| [forms.py](bluelog/forms.py)                               | 表单类                   |
| [settings.py](bluelog/settings.py)                         | 配置文件                  |
| [models.py](bluelog/models.py)                             | 数据模型                  |
| [utils.py](bluelog/utils.py)                               | 辅助函数（如安全地址跳转校验等）     |
| [bluelog/blueprints/admin.py](bluelog/blueprints/admin.py) | 后台 admin 蓝图模块         |
| [bluelog/blueprints/auth.py](bluelog/blueprints/auth.py)   | 后台登录认证蓝图模块            |
| [bluelog/blueprints/blog.py](bluelog/blueprints/blog.py)   | 前台 blog 蓝图模块          |
