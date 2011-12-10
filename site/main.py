import tornado.ioloop
import tornado.web
import tornado.template
import sqlite3

import pages

application = tornado.web.Application([
    (r'/', pages.Main),
    (r'/search', pages.Search),
    (r'/movie/(.*)', pages.Movie),
    (r'/serie/(.*)', pages.Serie),
    (r'/poster/(.+)/(.+)', pages.Poster),
    (r'/person/(.+)/(.+)/(.*)', pages.Person),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
