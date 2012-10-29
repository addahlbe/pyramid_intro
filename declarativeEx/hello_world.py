# DECLARATIVE CONFIGURATION
# WHY:
#   It's sometimes painful to have all configuration done by imerative code, because often the code for a single
# application may live in many files. If the configuration is centralized in one place, you'll need to have at least two files
# open at once to see the "big picture": the file that represents the configuration, and the file that contains the implemntation objects
# referenced by the configuration. To avoid this, Pyramid allows you to insert configuration decoration statements verry close to code that
# is refered to by the declaration itself.

from pyramid.response import Response 
from pyramid.view import view_config

@view_config(name='hello', request_method='GET')
def hello(request):
    return Response('Hello')
# The mere existence of configuration decoration doesn't cause any configuration registration to be performed. Before it has
# any effect on the configuration of a Pyramid application, a configuration decoration within application code must be found through a process
# known as a *scan*

# A scan of a module or a package and its subpackages for decorations happens when the pyramid.config.Configurator.scan() method is invoked:
# scanning implies seraching for configuration declarations in a package and its subpackages.