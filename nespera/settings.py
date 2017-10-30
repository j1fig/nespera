import os


ROOT_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '..'
)

DATABASE_URL = os.getenv('NESPERA_DB_URL')
