# celeryTest/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ruta para la página de inicio
    path('numbers/', include('numeros.urls')),
]
