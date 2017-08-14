#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print "aaaaaaaaaaaaaaaaaa"
        query=self.get_argument("q")
        print query

        client=tornado.httpclient.HTTPClient()
        response=client.fetch("http://search.twitter.com/search.json?"+urllib.urlencode(
           {"q":query,"result_type":"recent","rpp":100}))

        #body=json.loads(response.body)





        self.write('aaaa')

        #print body
        #result_count=len(body(["result"]))
        #now=datetime.datetime.utcow()
        #raw_oldest_tweet_at=body["results"][-1]["created_at"]
        ##oldest_tweet_at=datetime.datetime.strptime(raw_oldest_tweet_at,"%a,%d %b %Y %H:%M:%S +0000")
        #second_diff=time.mktime(now.timetuple())- \
#                    time.mktime(oldest_tweet_at.timetuple())

 #       tweets_per_second=float(result_count)/second_diff

        #self.write(r'<div style="text-align:center"> '
        #           r'<div style="font-size:72px">{}</div> '
        #           r'<div style="font-size:144px">{}</div>'
         #          r'<div style="font-size:24px">tweets per second</div>'
         #          r'</div> '.format(query,tweets_per_second))


if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[("/",IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()