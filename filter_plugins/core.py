from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.urlsplit import split_url

def slugify_repo(arg, slug='-'):
    return split_url(arg, 'path').lstrip('/').replace('/', slug)


class FilterModule(object):
    def filters(self):
        return {
            'slugify_repo': slugify_repo
        }

