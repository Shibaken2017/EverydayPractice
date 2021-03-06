#!/usr/bin/env python
# -*- coding: utf-
#get requestを受け取って、それを返すだけのprogram
import tornado.httpserver
import tornado.ioloop
import tornado.options

import tornado.web


from tornado.options import define ,options
define("port" ,default=7000,help="run on the given port",type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting=self.get_argument("greeting","hello")
        self.write("Hello,Udacity!")

if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




