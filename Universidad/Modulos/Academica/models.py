from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.PositiveSmallIntegerField(default=8)
    

    