from .base import *

DEBUG = False 

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1', '[::1]' ]
CSRF_TRUSTED_ORIGINS = ["http://localhost:1337", "https://nginx:1337"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eletrader',
        'USER': 'eletrader_user',
        'PASSWORD': 'eletrader_password',
        'HOST': 'db',
        'PORT': '5432'
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}
