from datetime import datetime

from .db import execute, connection


def create_feed_table():
    execute("""
        CREATE TABLE IF NOT EXISTS
            feed(id INTEGER PRIMARY KEY ASC,
                 url TEXT,
                 created timestamp
            )
    """)


def insert_feed(url, created=None):
    if not created:
        created = datetime.utcnow()
    execute("""
        INSERT INTO feed (?,?)
    """, url, created)


def get_all_feeds():
    cursor = connection.cursor()
    return cursor.execute("""
        SELECT id, url, created from feed
    """)
