from django.contrib import admin 
 
from .models import Tesis, Evaluador, Autor, PalabraClave
"""Configuracion para el adminitrador de Django, para que se vea bien"""
class EvaluadorInline(admin.StackedInline):     
    model = Evaluador     
    extra = 1

class AutorInline(admin.StackedInline):     
    model = Autor     
    extra = 1

class PalabraClaveInline(admin.StackedInline):     
    model = PalabraClave     
    extra = 1

class TesisAdmin(admin.ModelAdmin):
    fieldsets = [('Informacion de la tesis', {'fields': ['nombre','fecha','resumen', 'calificacion','estatus','escuela']}),]
    inlines = [PalabraClaveInline,EvaluadorInline,AutorInline] 
 
admin.site.register(Tesis, TesisAdmin) 
