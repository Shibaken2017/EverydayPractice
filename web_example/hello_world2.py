#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tornado.httpserver
import tornado.ioloop
import tornado.options

import tornado.web
import json
import datetime

from tornado.options import define ,options
define("port" ,default=7000,help="run on the given port",type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):

        #greeting=self.get_argument("greeting","hello")
        #
        #
        #
        d = datetime.datetime.today()
        t = "{}/{}/{} {}:{}:{}".format(d.year, d.month, d.day, d.hour, d.minute,d.second)
        dic = {"message": "hello_world!!", "recieved at": t}

        output= json.dumps(dic)


        self.write(output)

if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()





