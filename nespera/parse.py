#!/usr/bin/env python
"""
Script that takes md5 of the html of all stored pages in DB.
If not the same as the DB for that absolute URL, stores the md5 in the DB
and saves the html locally.
"""
import os
import sys
from setproctitle import setproctitle
from hashlib import md5
import logging

import requests
from requests.exceptions import ConnectionError
import redis

import settings


URLS = [
    (1, 1, 'http://www.cmjornal.pt/'),
]


def parse_page(url):
    """
    Gets the URL content and its MD5 digest.
    """
    r = requests.get(url)
    html_hash = md5()
    html_hash.update(r.content)
    return (r.content, html_hash.hexdigest())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        setproctitle(sys.argv[1])

    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    base_content_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        settings.BASE_CONTENT_DIR
    )

    while True:
        for s_id, p_id, u in URLS:
            try:
                html, page_hash = parse_page(u)
                hash_key = 'pages:%d:last_hash' % p_id
                cached_hash = r.get(hash_key)
                if cached_hash != page_hash:
                    content_path = os.path.join(
                        base_content_path,
                        str(p_id)
                    )
                    if not os.path.isdir(content_path):
                        os.makedirs(content_path)
                    html_filename = os.path.join(
                        content_path,
                        '%s.html' % page_hash
                    )
                    with open(html_filename, 'a') as f:
                        f.write(html)
                    r.set(hash_key, page_hash)
                logging.info('[parse] page_hash: %s; cached_hash: %s' % (page_hash, cached_hash))
            except ConnectionError:
                logging.error('[parse] error reaching URL %s' % u, exc_info=1)
