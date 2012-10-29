# WSGI protocol to connect an application and a web server together.
from wsgiref.simple_server import make_server
# The script imports the configurator class from the pyramid.congfig module.
# an instance of the Configurator class is later used to configure your Pyramid application.
from pyramid.config import Configurator
# created for later use: an instance of this class will be used to create a web response.
from pyramid.response import Response

# This function accepts a single argument (request) and it returns an instance of the pyramid.response.
# The single argument to the class' constructor is a string computed from parameters matched from the URL.
# This value becomes the body of the response.

# This function is know as a *view callable*. A view callable accepts a single argument: request. It 
# is expected to return a response object. A view callable doens't need to be a function; it can be
# represented via another type of object, like a class or an instance, but for our purposes here, a function serves us well.
def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

# The if __name__ == main line in the code sample above represents a python idiom: the code inside of this clause
# is not invoked unless the script containing this code is run directly from the operating system command line.
# for example the only way this code gets run is if I type python hello_world.py in the command prompt.
if __name__ == '__main__':
    # The config = Configurator() line creates an instance of the Conigurator class.
    # The resulting config object represents an API which the script uses to configure this particular Pyramid application.
    # methods called on the Configurator will cause registrations to be made in an application registry associated with the application.
    config = Configurator()
    # Line 29 call the pyramid.config.Configurator.add_route() method, which registers a route to match any URL path tht begins with /hello/
    # followed by a string.
    config.add_route('hello', '/hello/{name}')
    # Line 32 config.add_view(hello_world, route_name='hello'), registers hello_world function as a view callable and makes sure
    # that it will be called when the hello route is matched.
    config.add_view(hello_world, route_name='hello')
    # A call to make_wsgi_app implies that all configuration is finished.
    app = config.make_wsgi_app()
    # finally we actually serve the application to requestors by starting up a WSGI server.
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
