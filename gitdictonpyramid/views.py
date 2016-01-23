from pyramid.view import view_config, notfound_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound

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

@view_config(context=gitdict.File, name='history', renderer='templates/history.pt')
def git_file_history(context, request):
    # history is only available for text files
    mtype, encoding = mimetypes.guess_type(context.__name__)
    if mtype is None or not mtype.startswith('text/'):
        raise HTTPNotFound()
    # collect all commits except the current one
    old_commits = list(context.history)[1:]
    if old_commits:
        # get the diffs between the commits
        reference = context.last_commit
        changes = []
        for commit in old_commits:
            patch = context.diff(commit, reference=reference)
            changes.append((patch, reference))
            reference = commit
        # get the first commit and version of the file
        first_file_commit = old_commits[-1]
        first_pygit_file = context._get_object_from_commit(first_file_commit)
        first_file_content = first_pygit_file.data.decode('utf-8')
    else:
        # this file has no changes
        changes = []
        first_file_content = context.text
        first_file_commit = context.last_commit
    return {'changes': changes, 
            'first_file_content': first_file_content,
            'first_file_commit': first_file_commit}

@notfound_view_config(renderer='templates/404.pt')
def whoops(context, request):
    return {}