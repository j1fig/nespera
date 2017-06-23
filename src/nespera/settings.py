import os


BASE_CONTENT_DIR = 'content'

ROOT_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '..'
)

DB_SETTINGS = {
    'dev': {
        'host': 'localhost',
        'port': 5432,
        'user': 'nespera',
        'pass': 'nespera'
    },
}
