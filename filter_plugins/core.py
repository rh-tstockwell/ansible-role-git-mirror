from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.urlsplit import split_url
from six import string_types


def slugify(arg, slug='-'):
    return split_url(arg, 'path').lstrip('/').replace('/', slug)


# builds a map of src repo slugs to their destination
# handles lists of strings as well as lists of {src:, [dest:]}
def repo_map(mirrors, default_repo, slug='-'):
    mapped = {}
    for mirror in mirrors:
        if isinstance(mirror, dict):
            repo_slug = slugify(mirror['src'])
            mapped[repo_slug] = '{}/{}'.format(mirror['dest'] if 'dest' in mirror else default_repo, repo_slug)
        elif isinstance(mirror, string_types):
            repo_slug = slugify(mirror['src'])  # potentially redundant but being safe
            mapped[repo_slug] = '{}/{}'.format(default_repo, repo_slug)
    return mapped


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'slugify': slugify,
            'repo_map': repo_map
        }

