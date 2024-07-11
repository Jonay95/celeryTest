from django.db import models

class NumberRecord(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()

    class Meta:
        db_table = 'numeros_numberrecord'

    def __str__(self):
        return f"{self.number1} + {self.number2} = {self.result}"
