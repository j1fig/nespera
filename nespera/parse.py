#!/usr/bin/env python
"""
Script that takes md5 of the content of all feeds in DB.
If not the same as the DB for that absolute URL, stores the md5 in the DB
and saves the feed locally.
"""
import logging
import os
import sys
from hashlib import md5
from setproctitle import setproctitle
from time import sleep

import requests
from requests.exceptions import ConnectionError

from nespera.models.feed import get_all_feeds
from nespera.models.content import insert_content
from nespera.models import db
from nespera.utils.cache import feed_cache


def parse_page(url):
    """
    Gets the URL content and its MD5 digest.
    """
    r = requests.get(url)
    content_hash = md5(r.content)
    return (r.content.decode('iso-8859-1'), content_hash.hexdigest())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        setproctitle(sys.argv[1])

    db.create_tables()

    logging.info('[parse] starting daemon...')

    while True:
        for feed_id, url, _ in get_all_feeds():
            try:
                content, content_hash = parse_page(url)
                hash_key = 'feed:{}'.format(feed_id)
                cached_hash = feed_cache.get(hash_key)
                if cached_hash != content_hash:
                    _, __, created = insert_content(feed_id, content)
                    feed_cache.set(hash_key, content_hash)
                    logging.info('[parse] {}: new content detected for {}'.format(created, url)) 
            except ConnectionError:
                logging.error('[parse] error reaching URL {}'.format(url), exc_info=1)
        sleep(1)
