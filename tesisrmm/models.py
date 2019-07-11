from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum

class Status(Enum):
    Finalizado = "Finalizado"
    Ejecucion = "En ejecución"

class Tesis(models.Model):
    nombre = models.CharField(max_length=120)
    fecha = models.DateTimeField('fecha de publicación')
    resumen =  models.TextField()
    calificacion = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)])
    estatus = models.CharField(
      max_length=5,
      choices=[(tag, tag.value) for tag in Status]
    )
    escuela = models.CharField(max_length=120)
    
class Autor(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    correo = models.CharField(max_length=120)
    escuela = models.CharField(max_length=120)

class PalabraClave(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    palabra = models.CharField(max_length=120)

class Evaluador(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    tutor = models.BooleanField(default=False)


