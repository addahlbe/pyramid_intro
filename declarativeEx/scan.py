# Starting a Scan

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config()
def hello(request):
    return Response('This is the response!')

if __name__ == '__main__':
    from pyramid.config import Configurator
    config = Configurator()
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()