# numeros/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NumberRecord
from celeryTest.tasks import notify_db_change_task

@receiver(post_save, sender=NumberRecord)
def notify_db_change(sender, instance, **kwargs):
    notify_db_change_task.delay(instance.id, instance.number1, instance.number2, instance.result)
