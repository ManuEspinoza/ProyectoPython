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
                'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'autocomplete':'off'}),
                'calificacion': forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
                'estatus': forms.Select(attrs={'class': 'form-control', 'autocomplete':'off'}),
                'escuela': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
        }
        

class PalabraClaveForm(forms.ModelForm):

    class Meta:
        model = PalabraClave
        exclude = ('tesis',)

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        exclude = ('tesis',)

class EvaluadorForm(forms.ModelForm):

    class Meta:
        model = Evaluador
        exclude = ('tesis',)