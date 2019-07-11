from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Tesis(models.Model):
    OPTIONS = (
        ("Finalizado", "Finalizado"),
        ("En ejecución", "En ejecución"),
    )
    nombre = models.CharField(max_length=120)
    fecha = models.DateTimeField('fecha de publicación')
    resumen =  models.TextField()
    calificacion = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)])
    estatus = models.CharField(
      max_length=10,
      choices=OPTIONS
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


