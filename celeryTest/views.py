# celeryTest/views.py

from django.shortcuts import render, redirect
from numeros.forms import OperationForm
from numeros.models import NumberRecord

def home(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            operation.result = operation.number1 + operation.number2
            operation.save()
            return redirect('home')
    else:
        form = OperationForm()

    operations = NumberRecord.objects.all()  # Accede a la tabla correcta

    return render(request, 'home.html', {'form': form, 'operations': operations})
