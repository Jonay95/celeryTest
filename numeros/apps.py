# numeros/apps.py
from django.apps import AppConfig

class NumerosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'numeros'

    def ready(self):
        import numeros.signals
