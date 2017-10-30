"""
Just an in-memory cache for now, however all cache related things will stay in here.
"""


class Cache(object):

    def __init__(self):
        self._cache = {}

    def get(self, key):
        return self._cache.get(key, None)

    def set(self, key, value):
        self._cache[key] = value


feed_cache = Cache()
