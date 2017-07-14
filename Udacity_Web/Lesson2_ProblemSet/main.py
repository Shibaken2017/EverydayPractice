#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=9000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class MungedPageHandler(tornado.web.RequestHandler):
    def __rot13(self,c):
        if 'A' <= c and c <= 'Z':
            # 13 文字分ずらす
            return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))

        if 'a' <= c and c <= 'z':
            # 13 文字分ずらす
            return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))

        # その他の文字は対象外
        return c

    def rot13(self,s):
        # ジェネレータ内包表記で文字列に ROT13 を適用する
        g = (self.__rot13(c) for c in s)
        # 文字列に直す
        return ''.join(g)

    def map_by_first_letter(self,text):
        mapped=dict()
        for line in text.split("\r\n"):
            for word in [x for x in line.split(' ') if len(x)>0]:
                if word[0] not in mapped:
                    mapped[word[0]]=[]
                    mapped[word[0]].append(word)

    def post(self):
        source_txt=self.get_argument("source")
        output=self.rot13(source_txt)

        self.render("rot13.html",output=output)

if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers=[(r'/',IndexHandler),(r'/rot13',MungedPageHandler)],
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),debug=True)

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
