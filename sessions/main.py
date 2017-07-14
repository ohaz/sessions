from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
import os
from git import Repo

from app import app, debug, host, port
import views

if __name__ == '__main__':

    if not os.path.exists(os.path.join('git', 'sessionsTest')):
        repo = Repo.clone_from('https://github.com/ohaz/sessionsTest.git', to_path=os.path.join('git', 'sessionsTest'))
    else:
        repo = Repo(os.path.join('git', 'sessionsTest'))
    origin = repo.remotes.origin
    views.origin = origin
    origin.pull()
    if debug:
        app.run(debug=True, port=port, host=host)
    else:
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(port)
IOLoop.instance().start()
