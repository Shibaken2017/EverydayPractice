#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path

from tornado.options import define,options
define("port",default=8000,help=#run ont the given port,type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        self.set_secure_cookie("username",self.get_argument("username"))
        self.redirect("/")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html",user=self.current_user)

class LogOutHandler(BaseHandler):
    def get(self):
        if(self.get_argument("logout",None)):
            self.clear_cookie("username")
            self.redirect("/")

if __name__=="__main__":
    tornado.options.parse_command_line()
    settings={"template_path":os.path.join(os.path.dirname(__file__),"templates"),"cookie_secret":"9V8lRJ9zRBCLBHZlhnBCL18ydljl40doroM9S4p2ZMg="
              ,"xsrf_cok"}