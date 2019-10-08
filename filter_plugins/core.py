from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.filter.urlsplit import split_url


def slugify(arg, slug='-'):
    return split_url(arg, 'path').lstrip('/').replace('/', slug)


# builds a map of src repo slugs to their destination
def repo_map(mirrors, default_repo, slug='-'):
    def mapped = {}
    for mirror in mirrors:
        def repo_slug = slugify(mirror['src'])
        mapped[repo_slug] = mirror.has_key('dest') mirror['dest'] else '{}/{}'.format()default_repo + '/' + 
    return mapped
        
    return { ): mirror.has_key('dest') mirror.dest else default_repo +  for mirror in mirrors}


class FilterModule(object):
    def filters(self):
        return {
            'slugify': slugify,
            'repo_map': repo_map
        }

