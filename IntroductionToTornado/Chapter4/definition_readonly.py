#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sqlite3


DB_NAME="./test.db"
TABLE_NAME="practice"


from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)



class Application(tornado.web.Application):
    def __init__(self):
        conn=sqlite3.connect(DB_NAME)
        self.curs = conn.cursor()

        handlers=[(r"/(\w+)",WordHandler)]




class WordHandler(tornado.web.RequestHandler):

    def get(self,word):
        curs=self.application.curs
        checker = curs.execute("select count(*) from sqlite_master where type='table' and name='{}'".format(TABLE_NAME))
        if checker.fetchall()[0]==(0,):
            #there is no designated table in the db
            self.set_status(404)
            self.write({"error": "table:{} not found".format(TABLE_NAME)})
        word_doc=curs.execute("SELECT * FROM {} where word={}".format(TABLE_NAME,word))
        if word_doc:
            self.write(word_doc)

        else:
            self.set_status(404)
            self.write({"error":"{}not found".format(word)})

