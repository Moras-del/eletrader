from .base import *

DEBUG = True

ADMINS = (
    ('Szymon M', 'morekszymon@wp.pl'),
)

ALLOWED_HOSTS = ['eletrader.com', 'www.eletrader.com', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'eletraderdb',
#         'USER': 'eletraderuser',
#         'PASSWORD': 'eletraderpassword',
#     }
# }
MEDIA_ROOT = '/home/szymon/media'
STATIC_ROOT = '/home/szymon/static'
