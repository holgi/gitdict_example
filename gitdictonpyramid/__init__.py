from pyramid.config import Configurator

import os
import gitdict

def root_factory(request):
    git_repo_path = os.path.dirname(os.path.dirname(__file__))
    return gitdict.Repository(git_repo_path)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
