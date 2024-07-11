# celeryTest/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer la configuración predeterminada de Django para el módulo 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryTest.settings')

app = Celery('celeryTest')

# Usar la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks de todos los paquetes de aplicaciones Django
app.autodiscover_tasks()
