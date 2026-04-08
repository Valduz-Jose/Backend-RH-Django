from django.urls import path #Para definir las rutas de la API
from .views import EmpleadoListCreateView, EmpleadoRetrieveUpdateDestroyView #Importamos las vistas que hemos creado para manejar las solicitudes HTTP

urlpatterns = [
    path('api/empleados', EmpleadoListCreateView.as_view(), name='empleado-list-create'), #Ruta,vista y nombre de la ruta para listar y crear empleados
    #as_view() es un método que convierte la clase de vista en una función que puede ser llamada por Django cuando se recibe una solicitud HTTP en esa ruta específica. Esto es necesario porque Django espera que las vistas sean funciones, pero al usar clases basadas en vistas, necesitamos convertirlas a funciones para que Django pueda manejarlas correctamente.
    path('api/empleados/<int:pk>/', EmpleadoRetrieveUpdateDestroyView.as_view(), name='empleado-detail'),
]