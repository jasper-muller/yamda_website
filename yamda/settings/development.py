from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yamdb',
        'USER': os.getenv("YAMDA_USER_DEV"),
        'PASSWORD': os.getenv("YAMDA_KEY_DEV"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../core/static/yamda/img/')
