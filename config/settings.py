import os

DEBUG = os.environ.get('DEBUG', False)

HOST = os.environ.get('HOST', '127.0.0.1')

PORT = os.environ.get('PORT', 8080)

BLUEPRINTS = [
    'short_link',
]

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')

DB_PORT = os.environ.get('DB_PORT', 5432)

DB_NAME = os.environ.get('DB_NAME')

DB_USER_NAME = os.environ.get('DB_USER_NAME')

DB_USER_PASSWORD = os.environ.get('DB_USER_PASSWORD')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
