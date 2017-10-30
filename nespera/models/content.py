from datetime import datetime

from .db import execute, connection


def create_content_table():
    execute("""
        CREATE TABLE IF NOT EXISTS
            content(id INTEGER PRIMARY KEY ASC,
                 content TEXT,
                 created timestamp,
                 feed_id INTEGER,
                 FOREIGN KEY(feed_id) REFERENCES feed(id)
            )
    """)


def insert_content(feed_id, content, created=None):
    if not created:
        created = datetime.utcnow()
    execute("""
        INSERT INTO content(feed_id, content, created) VALUES (?,?,?)
    """, [feed_id, content, created])
    return feed_id, content, created


def get_content_by_feed_id(feed_id):
    cursor = connection.cursor()
    return cursor.execute("""
        SELECT * from feed
    """, url, created)
