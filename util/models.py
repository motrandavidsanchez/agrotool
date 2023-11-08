from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=150)
    codigo = models.IntegerField()

    def __str__(self):
        return self.name
