from pyramid.view import view_config
from pyramid.response import Response

import gitdict
import io
import mimetypes


@view_config(context=gitdict.Repository, renderer='templates/folder.pt')
@view_config(context=gitdict.Folder, renderer='templates/folder.pt')
def git_folder(context, request):
    items = [context[key] for key in sorted(context)]
    return {'items': items}

@view_config(context=gitdict.File, renderer='templates/file.pt')
def git_file(context, request):
    return {}

@view_config(context=gitdict.File, name='download')
def git_file_download(context, request):
    mtype, encoding = mimetypes.guess_type(context.__name__)
    return Response(body=context.data, content_type=mtype)
