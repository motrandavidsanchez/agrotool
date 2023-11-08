from django.db import models

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
    objetive = models.CharField(max_length=5, choices=OBJECTIVE, blank=True, null=True, verbose_name='Objetivo')
    hectare = models.ForeignKey(Hectare, on_delete=models.CASCADE)

    def __str__(self):
        return f'Lote ({self.code})'
