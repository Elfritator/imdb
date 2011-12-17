import tornado.ioloop
import tornado.web
import tornado.template
import sqlite3
import os.path
import pages

settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': 'N53gLGkySeCvX5AjgUgmtAez7L8JhUP2hb+MYgizGWo=',
    'xsrf_cookies': True,
    'debug': True
}

application = tornado.web.Application([
    (r'/', pages.Main),
    (r'/search', pages.Search),
    (r'/search_results/(.*)', pages.SearchResults),
    (r'/movie/(.*)', pages.Movie),
    (r'/serie/(.*)', pages.Serie),
    (r'/episode/(.*)', pages.Episode),
    (r'/person/(.+)/(.+)/(.*)', pages.Person),
    (r'/poster/(.+)/(.+)', pages.Poster),
    (r'/location/(.+)', pages.Location),
    (r'/(up|down)vote/(.*)', pages.Vote),
    (r'/admin', pages.AdminPanel),
    (r'/admin/login', pages.AdminLogin),
    (r'/admin/logout', pages.AdminLogout),
    (r'/admin/add', pages.AdminAdd),
    (r'/admin/add/(movie|serie|episode)', pages.AdminAddWork),
    (r'/admin/add/(director|writer|actor)', pages.AdminAddPerson),
    (r'/admin/add/(genre|country|language)', pages.AdminAddInfo),
    (r'/admin/delete', pages.AdminDelete),
    (r'/admin/delete/work/(.*)', pages.AdminDeleteWork),
    (r'/admin/delete/person/(.+)/(.+)/(.*)', pages.AdminDeletePerson),
    (r'/admin/delete/(director|writer|actor)/(.+)/(.+)/(.*)/(.+)/?(.*)', pages.AdminDeletePersonType),
    (r'/admin/delete/(genre|country|language)', pages.AdminDeleteInfo)
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
