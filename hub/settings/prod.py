# flake8: noqa

import os

from hub.settings.common import *

def read_secret(secret_name, file_name):
    target = os.path.join('/run/secrets/', secret_name, file_name)
    with open(target) as f:
        return f.read()


DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = read_secret('hub-web', 'hub-web-secret-key.txt')
ALLOWED_HOSTS = ['hub.local']
AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hub',
        'USER': read_secret('hub-db', 'hub-db-username.txt'),
        'PASSWORD': read_secret('hub-db', 'hub-db-password.txt'),
        'HOST': 'hub-db.default.svc.cluster.local',
        'PORT': '5432',
    }
}

MEDIA_ROOT = '/media/'
