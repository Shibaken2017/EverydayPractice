#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import datetime
import time

import urllib
import json
import datetime
import time


from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query=self.get_argument("q")
        client=tornado.httpclient.AsyncHTTPClient()
        response=yield tornado.gen.Task()client.fetch,"http://search.twitter.com"


