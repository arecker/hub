# flake8: noqa

import os

from hub.settings.common import (
    BASE_DIR, INSTALLED_APPS, MIDDLEWARE,
    ROOT_URLCONF, TEMPLATES, WSGI_APPLICATION,
    LANGUAGE_CODE, TIME_ZONE,
    USE_I18N, USE_L10N, USE_TZ,
    STATIC_URL
)

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
