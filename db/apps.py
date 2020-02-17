from django.apps import AppConfig


class DbConfig(AppConfig):
    name = 'db'

    def ready(self):
        from . import signals  # noqa
