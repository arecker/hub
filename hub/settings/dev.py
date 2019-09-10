# flake8: noqa

import os

from hub.settings.common import *

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'blessed-be-the-fruit'
AUTH_PASSWORD_VALIDATORS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tmp/db.sqlite3')
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/email')
