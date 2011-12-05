import tornado.ioloop
import tornado.web
import tornado.template
import sqlite3

class Movie(tornado.web.RequestHandler):
    def get(self, movie_id):
        loader = tornado.template.Loader('templates/')
        
        conn = sqlite3.connect('db.sqlite')
        cur = conn.cursor()
      
        # fetch the movie
        cur.execute('select Title, Year, Note from Work where ID = ?',
                    (movie_id,))
        movie = cur.fetchone()
      
        if movie:
            # fetch the actors
            cur.execute('select FirstName, LastName, Num, Role from Actor where ID = ?',
                        (movie_id,))
            actors = cur.fetchall()
          
            # fetch the directors
            cur.execute('select FirstName, LastName, Num from Director where ID = ?',
                        (movie_id,))
            directors = cur.fetchall()
          
            # fetch the writers
            cur.execute('select FirstName, LastName, Num from Director where ID = ?',
                        (movie_id,))
            writers = cur.fetchall()
          
            # fetch the countries
            cur.execute('select Country from Country where ID = ?',
                        (movie_id,))
            countries = map(lambda x: x[0], cur.fetchall())
          
            # fetch the languages
            cur.execute('select Language from Language where ID = ?',
                        (movie_id,))
            languages = map(lambda x: x[0], cur.fetchall())
          
            # fetch the genres
            cur.execute('select Genre from Genre where ID = ?',
                        (movie_id,))
            genres = map(lambda x: x[0], cur.fetchall())
          
            cur.close()
          
            self.write(loader.load('movie.html').generate(movie=movie, 
                                                          actors=actors,
                                                          directors=directors,
                                                          writers=writers,
                                                          countries=countries,
                                                          languages=languages,
                                                          genres=genres))
        else:
            self.write(loader.load('not_found.html').generate(message='Movie \'' +
                                                              movie_id +
                                                              '\' not found'))
