from django import forms

class SumForm(forms.Form):
    number1 = forms.IntegerField(label='Número 1')
    number2 = forms.IntegerField(label='Número 2')
