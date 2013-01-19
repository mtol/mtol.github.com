from os import walk
from sys import exit
from fnmatch import fnmatch


def pages(pages_path):
    """The base HTML files within the template director.
    Avoids using those inherited by other templates.
    """
    base = None
    pages = {}

    for path, dirs, files in walk(pages_path):
        if not base:
            base = len(path)+1
        for name in files:
            if fnmatch(name, "*.html"):
                f = "%s/%s" % (path, name)
                pages[f] = f[base:]

    return pages
