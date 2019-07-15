from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

"""Modelos para el proyecto son autoexplicativos"""
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
      max_length=15,
      choices=OPTIONS
    )
    escuela = models.CharField(max_length=120)
    
class Autor(models.Model):
    aut_tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    aut_nombre = models.CharField(max_length=120)
    aut_apellido = models.CharField(max_length=120)
    aut_correo = models.CharField(max_length=120)
    aut_escuela = models.CharField(max_length=120)

class PalabraClave(models.Model):
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    palabra = models.CharField(max_length=120)

class Evaluador(models.Model):
    eva_tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE) 
    eva_nombre = models.CharField(max_length=120)
    eva_apellido = models.CharField(max_length=120)
    eva_tutor = models.BooleanField(default=False)


