# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
urls = (
    '/wx', 'Handle',
    '/', 'index',
)


class index(object):
    def GET(self):

        return "这是公众测试页面！this is handle view!"


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
