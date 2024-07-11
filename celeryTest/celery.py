# celeryTest/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el entorno de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryTest.settings')

app = Celery('celeryTest')

# Usar el archivo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir tareas en todas las aplicaciones de Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Configurar tareas periódicas
app.conf.beat_schedule = {
    'print-every-10-seconds': {
        'task': 'celeryTest.tasks.print_message',
        'schedule': 10.0,  
        'args': ()
    },

}
app.conf.timezone = 'Europe/Madrid'
