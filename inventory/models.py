from django.db import models

from staff.models import Staff
from util.models import BaseModel


class Tool(BaseModel):
    class Meta:
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    owner = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Propietario')


class StaffEquipment(BaseModel):
    class Meta:
        verbose_name = 'Equipo para personal'
        verbose_name_plural = 'Equipos para personal'


class Supplies(BaseModel):
    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
