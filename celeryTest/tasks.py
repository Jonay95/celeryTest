# celeryTest/tasks.py
from datetime import datetime 
from celery import shared_task
from numeros.models import NumberRecord

@shared_task
def add(x, y):
    return x + y

@shared_task
def print_message():
    try:
        record = NumberRecord.objects.get(id=1)
        print(f"hola mundo, {datetime.now()}, Resultado: {record.result}")
    except NumberRecord.DoesNotExist:
        print("Registro con ID 1 no encontrado.")
