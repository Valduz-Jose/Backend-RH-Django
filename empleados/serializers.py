from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']

    def validate_nombre(self, value):
        v = (value or "").strip()
        if not v:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return v

    def validate_departamento(self, value):
        v = (value or "").strip()
        if not v:
            raise serializers.ValidationError("El departamento no puede estar vacío.")
        return v

    def validate_sueldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor a 0.")
        return value