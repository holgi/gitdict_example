from pyramid.view import view_config

import gitdict

@view_config(context=gitdict.Repository, renderer='templates/repository.pt')
def repository(context, request):
    items = [context[key] for key in sorted(context)]
    return {'items': items}

@view_config(context=gitdict.Folder, renderer='templates/mytemplate.pt')
def folder(context, request):
    return {}

@view_config(context=gitdict.File, renderer='templates/mytemplate.pt')
def folder(context, request):
    return {}
