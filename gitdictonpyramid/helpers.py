import datetime
import gitdict
import pyramid.location
import mimetypes

def first_line(text):
    ''' returns the first line of a multiline text '''
    return text.split('\n')[0]

def is_file(item):
    return isinstance(item, gitdict.File)

def parents(resource):
    ''' returns all parents of a resource
    
    starts with the root object and excludes the resource itself
    '''
    lineage = list(pyramid.location.lineage(resource))
    return list(reversed(lineage))[:-1]

def guess_type(resource):
    ''' guesses the mimetype of a resource and returns the top type part '''
    mtype, encoding = mimetypes.guess_type(resource.__name__)
    if mtype is None:
        return mtype
    top, sub = mtype.split('/', 1)
    return top