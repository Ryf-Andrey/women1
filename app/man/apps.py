from django.apps import AppConfig


class ManConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'man'

    verbose_name = 'Люди Мира' #'man.apps.ManConfig' 