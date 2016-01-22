import datetime
import gitdict
import pyramid.location

def first_line(text):
    return text.split('\n')[0]

def is_file(item):
    return isinstance(item, gitdict.File)

def parents(resource):
    lineage = list(pyramid.location.lineage(resource))
    return list(reversed(lineage))[:-1]