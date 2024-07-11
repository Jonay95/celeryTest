# numeros/views.py

from django.shortcuts import render, redirect
from .models import NumberRecord

def add_numbers(request):
    if request.method == "POST":
        number1 = request.POST.get("number1")
        number2 = request.POST.get("number2")
        NumberRecord.objects.create(number1=number1, number2=number2)
        return redirect('add_numbers')

    return render(request, "add_numbers.html")
