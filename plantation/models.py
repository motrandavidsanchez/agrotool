from django.db import models
from django.utils import timezone

from plantation.constants import OBJECTIVE


class Hectare(models.Model):
    class Meta:
        verbose_name = 'Hectarea'
        verbose_name_plural = 'Hectareas'

    code = models.CharField(max_length=150, verbose_name='Codigo')

    def __str__(self):
        return f'Hectarea ({self.code})'


class Batch(models.Model):
    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    code = models.CharField(max_length=150, verbose_name='Codigo')
    tree_age = models.IntegerField(verbose_name='Edad de arboles')
    species = models.CharField(max_length=150, verbose_name='Especie')
    quantity = models.IntegerField(blank=True, null=True, verbose_name='Cantidad')
    objetive = models.CharField(max_length=5, choices=OBJECTIVE, blank=True, null=True, verbose_name='Objetivo')
    hectare = models.ForeignKey(Hectare, on_delete=models.CASCADE)
    planting_date = models.DateField(verbose_name="Fecha de plantación", default=timezone.now)
    pruning_date = models.DateField(blank=True, null=True, verbose_name="Fecha de poda")

    def __str__(self):
        return f'Lote ({self.code})'
