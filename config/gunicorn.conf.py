import os

worker_class = 'gthread'
bind = ['0.0.0.0:8000']
reload = os.environ.get('DEBUG', True)