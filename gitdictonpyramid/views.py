from pyramid.view import view_config

import gitdict

@view_config(context=gitdict.Repository, renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'GitDictOnPyramid'}
