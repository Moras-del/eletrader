from .base import *

DEBUG = False

ALLOWED_HOSTS = ['eletrader.com', 'www.eletrader.com', 'localhost']

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

# MEDIA_ROOT = '/home/szymon/media'
# STATIC_ROOT = '/home/szymon/static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
