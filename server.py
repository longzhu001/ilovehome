# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
from .config import *
import redis
import torndb
from handlers import Passport
from .urls import urls
from tornado.options import options, define
from tornado.web import RequestHandler
#这是默认的端口,如果端口被控制,会自动调用其他的端口
define("port", default=8000, type=int, help="run server on the given port")


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        #链接数据库
        self.db = torndb.Connection(mysql_options)
        #链接redis缓存数据库
        self.redis = redis.StrictRedis(redis_options)


def main():
    options.log_file_prefix = log_path
    options.logging = log_level
    tornado.options.parse_command_line()
    app = Application(
        urls,
        settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()