from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINGE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}