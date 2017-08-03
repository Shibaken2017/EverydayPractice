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

DB_NAME = "./test.db"
TABLE_NAME = "practice"

from tornado.options import define, options

define("port", default=8000, help="run on the given port")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class EntrancePageHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title")
        content = self.get_argument("content")

        self.render("confirmation.html", title=title, content=content)


class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        '''
        コメントをdbに登録して,登録が完了したことを知らせる。
        :return:
        '''
        title = self.get_argument("title")
        content = self.get_argument("content")
        self.save(title,content)
        self.render("register.html")


    def save(self, title, text):
        '''
        save title and conttent to the db file
        :param title:
        :param content:
        :return:
        '''
        conn = sqlite3.connect(DB_NAME)
        curs = conn.cursor()
        # check whether the table "practice" already exists
        count = curs.execute("select count(*) from sqlite_master where type='table' and name='practice'")
        if count.fetchall()[0] == (0,):
            # create table
            curs.execute('''CREATE TABLE practice(date TIMESTAMP,title VARCHAR(50),text VARCHAR(50))''')

        d = datetime.datetime.today()
        now = d.strftime("%Y-%m-%d %H:%M:%S")
        ins = "INSERT INTO practice ( date,title,text)VALUES (?,?,?)"
        curs.execute(ins, (now, title, text))

        conn.commit()

        curs.close()
        conn.close()



class BoardHandler(tornado.web.RequestHandler):
    def get(self):
        '''
        掲示板が表示されるように返す!
        :return: 
        '''''
        print("return a board")
        self.extract()
        self.render("board.html",comments=self.output_txt)


    def extract(self):
        '''
        extract 10users data from db
        :return:
        '''
        if not os.path.exists(DB_NAME):
            raise Exception("designated db doesnt exist!")

        conn = sqlite3.connect(DB_NAME)
        curs = conn.cursor()

        curs.execute("SELECT * FROM practice")
        self.database = curs.fetchall()
        self.database.reverse()
        self.__change_list_to_text()
        curs.close()
        conn.close()


    def __change_list_to_text(self):
        '''
         change list extracted from sqlite3 ,which is list form ,to text style
        :param self:
        :return:
        '''
        self.output_txt = ""
        num = 0
        if len(self.database) > 0:
            for ele in self.database:
                if num == 10:
                    break
                num += 1
                self.output_txt += "title:{} content:{} date:{}".format(ele[1], ele[2],ele[0])


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler),
                                            (r'/confirmation', EntrancePageHandler)
        , (r'/register', RegisterHandler),(r'/boards',BoardHandler)],
                                  template_path=os.path.join(os.path.dirname(__file__), "templates"),
                                  static_path=os.path.join(os.path.dirname(__file__), "static"),
                                  debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
