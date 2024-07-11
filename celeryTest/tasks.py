# celeryTest/tasks.py
from datetime import datetime 
from celery import shared_task
from numeros.models import NumberRecord

@shared_task
def add(x, y):
    return x + y

@shared_task
def notify_db_change_task(record_id, number1, number2, result):
    try:
       print(f"CAMBIO EN BASE DE DATOS REGISTRADO: ID={record_id}, number1={number1}, number2={number2}, result={result}")
    except NumberRecord.DoesNotExist:
        print("Registro con ID 1 no encontrado.")
