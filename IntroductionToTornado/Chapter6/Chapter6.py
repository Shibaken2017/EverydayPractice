#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver

import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define,options
define("port",default=9000,help="run on the given port",type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cokie=self.get_secure_cookie("count")
        count=int(cokie)+1 if cokie else 1

        countString="1 time" if count==1 else "{} times".format(count)

        self.set_secure_cookie("count",str(count))
        self.write(r'<html><head><title>Cookie counter</title></head>'
                   r'<body><h1>you viewd this page {}times</h1>'
                   r'</body></html'.format(countString))


if __name__=="__main__":
    tornado.options.parse_command_line()
    settings={"cookie_secret":"laxGHrjeTkK5EVQIxtumpRV+riAoBkYzuMds/FRTMx8="}
    application=tornado.web.Application([(r'/',MainHandler)],**settings)
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()