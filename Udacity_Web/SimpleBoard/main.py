#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os.path
import random
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sqlite3
import datetime
from Comment import Comment






from tornado.options import define, options

define("port", default=8000, help="run on the given port")


class BoardHandler(tornado.web.RequestHandler):
    def get(self):
        '''
        掲示板が表示されるように返す!
        :return: 
        '''''
        print("return a board")


        self.comment_list=[Comment("12/32","uwaaa","jingisukan"),Comment("21/32","waaa","udon"),Comment("11/32","uuuuu","soba")]


        self.render("board.html",comment_list=self.comment_list)




if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', BoardHandler)],
                                  template_path=os.path.join(os.path.dirname(__file__), "templates"),
                                  static_path=os.path.join(os.path.dirname(__file__), "static"),
                                  debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

