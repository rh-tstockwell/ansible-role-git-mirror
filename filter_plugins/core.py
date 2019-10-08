from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.urlsplit import split_url


def slugify(arg, slug='-'):
    return split_url(arg, 'path').lstrip('/').replace('/', slug)


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'slugify': slugify,
        }

