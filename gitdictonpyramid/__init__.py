from pyramid.config import Configurator
from pyramid.events import BeforeRender

from . import helpers

import os
import gitdict
import mimetypes


def root_factory(request):
    git_repo_path = os.path.dirname(os.path.dirname(__file__))
    return gitdict.Repository(git_repo_path)

def add_render_helper(event):
    event['h'] = helpers

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_subscriber(add_render_helper, BeforeRender)
    config.scan()
    # these mimetypes will be used in file.pt
    mimetypes.add_type('text/template', '.pt')
    mimetypes.add_type('text/config', '.ini')
    mimetypes.add_type('text/markdown', '.md')
    return config.make_wsgi_app()
