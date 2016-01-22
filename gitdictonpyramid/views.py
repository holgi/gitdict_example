from pyramid.view import view_config

import gitdict

@view_config(context=gitdict.Repository, renderer='templates/folder.pt')
@view_config(context=gitdict.Folder, renderer='templates/folder.pt')
def git_folder(context, request):
    items = [context[key] for key in sorted(context)]
    return {'items': items}

@view_config(context=gitdict.File, renderer='templates/file.pt')
def git_file(context, request):
    return {}
