from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'blessed-be-the-fruit'
AUTH_PASSWORD_VALIDATORS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3',
    }
}
