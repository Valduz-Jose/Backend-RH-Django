from django.db import models

# Modelo aplicando el concepto de ORM
class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    departamento = models.CharField(max_length=100, null=False, blank=False)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'empleado' # Fuerza el nombre de la tabla en MySQL

    def __str__(self):
        return f"{self.nombre} - {self.departamento}"