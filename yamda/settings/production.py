from .base import *

DEBUG = False
ALLOWED_HOSTS = ['.yamda.nl']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("YAMDA_DB_PROD"),
        'USER': os.getenv("YAMDA_USER_PROD"),
        'PASSWORD': os.getenv("YAMDA_KEY_PROD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../core/static/yamda/img/')


