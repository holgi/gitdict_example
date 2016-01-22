import datetime
import gitdict

def first_line(text):
    return text.split('\n')[0]

def is_file(item):
    return isinstance(item, gitdict.File)