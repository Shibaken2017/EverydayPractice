
import tornado.httpserver
import tornado.ioloop

import tornado.options
import os
import tornado.web


from tornado.options import define,options
define("port",default=9000,help="run on the given port" ,type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        num=self.get_argument("num",1)

        self.render("fizzbuzz.html",num=num)


if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r"/",MainHandler)],template_path=os.path.join(os.path.dirname(__file__),"templates"))
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


