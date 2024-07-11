from django.shortcuts import render
from numeros.models import NumberRecord
from numeros.forms import SumForm
def home(request):
    if request.method == 'POST':
        form = SumForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            result = number1 + number2
            # Guarda el resultado en la base de datos
            NumberRecord.objects.create(number1=number1, number2=number2, result=result)
    else:
        form = SumForm()

    # Obtener todas las operaciones guardadas
    operations = NumberRecord.objects.all()

    return render(request, 'home.html', {'form': form, 'operations': operations})