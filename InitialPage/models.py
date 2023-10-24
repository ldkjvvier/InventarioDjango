from django.db import models

class Proyecto(models.Model):
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()
