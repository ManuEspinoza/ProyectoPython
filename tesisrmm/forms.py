from django import forms
from .models import Tesis, Evaluador, Autor, PalabraClave
from tempus_dominus.widgets import DatePicker

class StyledErrorForm(forms.Form):
    def is_valid(self):
        ret = forms.Form.is_valid(self)
        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': self.fields[f].widget.attrs.get('class', '') + ' is-invalid'})
        return ret

class TesisForm(forms.ModelForm, StyledErrorForm):
    fecha = forms.DateField(widget=DatePicker(attrs={'autocomplete':'off'}))
    class Meta:
        model = Tesis
        fields = '__all__'
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off', 'required':'false'}),
                'resumen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resumen', 'rows':3, 'autocomplete':'off', 'required':'false'}),
                'calificacion': forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off', 'required':'false'}),
                'estatus': forms.Select(attrs={'class': 'form-control', 'autocomplete':'off'}),
                'escuela': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escuela', 'autocomplete':'off', 'required':'false'}),
        }
        labels = {
            'fecha': ('Fecha de publicación'),
        }
        

class PalabraClaveForm(forms.ModelForm):

    class Meta:
        model = PalabraClave
        exclude = ('tesis',)
        widgets = {
                'palabra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Palabra', 'autocomplete':'off', 'required':'false'}),
        }
        

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        exclude = ('aut_tesis',)
        widgets = {
                'aut_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off', 'required':'false'}),
                'aut_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off', 'required':'false'}),
                'aut_correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo', 'autocomplete':'off', 'required':'false'}),
                'aut_escuela': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escuela', 'autocomplete':'off', 'required':'false'}),
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
                'eva_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off', 'required':'false'}),
                'eva_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off', 'required':'false'}),
        }
        labels = {
            'eva_nombre': ('Nombre'),
            'eva_apellido': ('Apellido'),
            'eva_tutor': ('Tutor'),
        }

class BuscadorForm(forms.Form):
    palabra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar'}), max_length=100,label='')

