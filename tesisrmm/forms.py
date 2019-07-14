from django import forms
from .models import Tesis, Evaluador, Autor, PalabraClave
from tempus_dominus.widgets import DatePicker

class TesisForm(forms.ModelForm):
    fecha = forms.DateField(widget=DatePicker(attrs={'autocomplete':'off'}))
    class Meta:
        model = Tesis
        fields = '__all__'
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}),
                'resumen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resumen', 'rows':3, 'autocomplete':'off'}),
                'calificacion': forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
                'estatus': forms.Select(attrs={'class': 'form-control', 'autocomplete':'off'}),
                'escuela': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escuela', 'autocomplete':'off'}),
        }
        labels = {
            'fecha': ('Fecha de publicación'),
        }
        

class PalabraClaveForm(forms.ModelForm):

    class Meta:
        model = PalabraClave
        exclude = ('tesis',)
        widgets = {
                'palabra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Palabra', 'autocomplete':'off'}),
        }
        

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        exclude = ('aut_tesis',)
        widgets = {
                'aut_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}),
                'aut_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off'}),
                'aut_correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo', 'autocomplete':'off'}),
                'aut_escuela': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escuela', 'autocomplete':'off'}),
        }
        labels = {
            'aut_nombre': ('Nombre'),
            'aut_apellido': ('Apellido'),
            'aut_correo': ('Correo'),
            'aut_escuela': ('Escuela'),
        }

class EvaluadorForm(forms.ModelForm):

    class Meta:
        model = Evaluador
        exclude = ('eva_tesis',)
        widgets = {
                'eva_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}),
                'eva_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off'}),
        }
        labels = {
            'eva_nombre': ('Nombre'),
            'eva_apellido': ('Apellido'),
            'eva_tutor': ('Tutor'),
        }
