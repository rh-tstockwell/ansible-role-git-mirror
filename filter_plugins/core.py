from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.urlsplit import split_url

def slugify(arg, slug='-'):
    if isinstance(arg, list):
        return map(_slug, arg, slug)
    else:
        return _slug(arg, slug)

def _slug(arg):
    return split_url(arg, 'path').lstrip('/').replace('/', slug)



class FilterModule(object):
    def filters(self):
        return {
            'slugify': slugify
        }

