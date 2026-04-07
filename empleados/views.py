from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

# Vista para listar todos los empleados y crear uno nuevo (GET, POST)
class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all().order_by('idEmpleado')
    serializer_class = EmpleadoSerializer

# Vista para obtener, actualizar o eliminar un empleado específico (GET, PUT, DELETE)
class EmpleadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'idEmpleado' #llave primaria del modelo Empleado