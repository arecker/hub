# flake8: noqa

from hub.settings.common import (
    BASE_DIR, INSTALLED_APPS, MIDDLEWARE,
    ROOT_URLCONF, TEMPLATES, WSGI_APPLICATION,
    LANGUAGE_CODE, TIME_ZONE,
    USE_I18N, USE_L10N, USE_TZ,
    STATIC_URL
)

DEBUG = False
SECRET_KEY = 'TODO-MAKE-BETTER'
ALLOWED_HOSTS = []
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]
