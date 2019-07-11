from django import forms
from .models import Tesis, Evaluador, Autor, PalabraClave

class TesisForm(forms.ModelForm):

    class Meta:
        model = Tesis
        fields = '__all__'

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