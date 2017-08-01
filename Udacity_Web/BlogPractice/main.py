import os.path
import random
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web



from tornado.options import   define,options
define("port",default=8000,help="run on the given port")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class EntrancePageHandler(tornado.web.RequestHandler):
    def post(self):
        title=self.get_argument("title")
        content=self.get_argument("content")

        self.render("confirmation.html",title=title,content=content)



class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        print self.get_argument("title")
        print self.get_argument("content")
        self.render("register.html")


if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r'/',IndexHandler),
                                          (r'/confirmation',EntrancePageHandler)
                                          ,(r'/register',RegisterHandler)],template_path=os.path.join(os.path.dirname(__file__),"templates"),
                                                                                                 static_path=os.path.join(os.path.dirname(__file__),"static"),
                                debug=True)

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
