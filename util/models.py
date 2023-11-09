from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    codigo = models.IntegerField(verbose_name='Codigo')

    def __str__(self):
        return self.name
