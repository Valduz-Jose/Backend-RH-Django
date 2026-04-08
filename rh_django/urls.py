from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta base de nuestra API delegada a la app empleados
    path('', include('empleados.urls')),#incluye las rutas definidas en empleados/urls.py para que estén disponibles en la aplicación principal
]