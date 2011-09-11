from copy import copy
from utils.sort import prepare_sort

_repository_sort_map = dict(
    name = 'slug_sort',
    owner = 'owner__slug_sort',
    updated = 'official_modified',
)
_account_sort_map = dict(
    name = 'slug_sort',
)

def get_repository_sort(key, allow_owner=True, default='name', default_reverse=False):
    """
    Return needed informations about sorting repositories
    """
    repository_sort_map = copy(_repository_sort_map)

    if not allow_owner:
        del repository_sort_map['owner']

    return prepare_sort(key, repository_sort_map, default, default_reverse)

def get_account_sort(key, default='name', default_reverse=False):
    """
    Return needed informations about sorting accounts
    """
    return prepare_sort(key, _account_sort_map, default, default_reverse)
