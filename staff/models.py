from django.db import models


class Staff(models.Model):
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=150, verbose_name='Apellido')
    dni = models.CharField(max_length=10, verbose_name='DNI')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefono')

    def __str__(self):
        return f'{self.name}, {self.last_name}'
