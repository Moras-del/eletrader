from .base import *

DEBUG = False

ADMINS = (
    ('Szymon M', 'morekszymon@wp.pl'),
)

ALLOWED_HOSTS = ['eletrader.com', 'www.eletrader.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eletraderdb',
        'USER': 'eletraderuser',
        'PASSWORD': 'eletraderpassword',
    }
}