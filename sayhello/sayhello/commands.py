# coding: utf-8
"""
    Author: Tyou
"""

# 命令行操作包：相比于内置的标准命令行库 Argparse 更简单
import click

from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='删除数据库并重新新建')
def initdb(drop):
    """
        初始化数据库
    """
    if drop:
        click.confirm("本操作将执行删除数据库，请确认是否继续", abort=True)
        db.drop_all()
        click.echo('数据库已删除完毕')
    db.create_all()
    click.echo('数据已创建/初始化完毕')


@app.cli.command()
@click.option('--count', default=20, help='生成信息数量，默认20条')
def forge(count):
    """
        初始化数据库，并生成初始测试数据
    """
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker('zh_CN')
    click.echo('模拟数据生成就绪。。。')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo("测试数据已生成完毕，总计 %s 条" % count)
