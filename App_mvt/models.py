from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre_completo = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    nro_tel = models.IntegerField()
    edad = models.IntegerField()