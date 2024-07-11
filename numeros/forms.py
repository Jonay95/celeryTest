# numbersapp/forms.py

from django import forms
from .models import NumberRecord

class OperationForm(forms.ModelForm):
    class Meta:
        model = NumberRecord
        fields = ['number1', 'number2']
