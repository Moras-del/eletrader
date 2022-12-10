from .base import *

DEBUG = True

ALLOWED_HOSTS = ['eletrader.com', 'www.eletrader.com', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eletrader',
        'USER': 'eletrader_user',
        'PASSWORD': 'eletrader_password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
