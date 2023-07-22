from django.apps import AppConfig


class IneffableAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ineffable_app'
