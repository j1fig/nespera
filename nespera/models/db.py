"""
Encapsulates and exposes all the DB related interfaces
"""
import sqlite3
import logging

from nespera import settings


def execute(sql, *args):
    try:
        with connection:
            connection.execute(sql, *args)
    except sqlite3.Error:
        logging.error('[nespera] Database Error', exc_info=1)
        raise


def create_tables():
    from .feed import create_feed_table
    from .content import create_content_table
    create_feed_table()
    create_content_table()


connection = sqlite3.connect(settings.DATABASE_URL)
