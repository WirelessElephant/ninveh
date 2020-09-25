import os
import dj_database_url

DB_URL = dj_database_url.parse(os.environ.get('PRIMARY_DATABASE_URL', '').replace('\n', ''))

DATABASES = {
    "default": DB_URL
}

SECRET_KEY = 'b2FpdWJlYmFoYXNkZmVnYnJhaGVhZ2VhZmVmCg=='

DEBUG = os.environ.get('DEBUG', True)