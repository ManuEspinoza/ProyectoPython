from django.http import HttpResponse
from django.shortcuts import render
from .forms import TesisForm, PalabraClaveForm, AutorForm, EvaluadorForm
from .models import Tesis

def index(request):
    tesis = Tesis.objects.all()[:5]
    return render(request, 'tesisrmm/inicio.html',{'tesis': tesis})

def create(request):
    if request.method == "POST":
        tesisform = TesisForm(request.POST)
        autorform = AutorForm(request.POST)
        evaluadorform = EvaluadorForm(request.POST)
        palabraform = PalabraClaveForm(request.POST)
        if tesisform.is_valid() and autorform.is_valid() and evaluadorform.is_valid() and palabraform.is_valid():
            tesis = tesisform.save()
            autor = autorform.save(commit=False)
            autor.aut_tesis = tesis
            autor.save()
            evaluador = evaluadorform.save(commit=False)
            evaluador.eva_tesis = tesis
            evaluador.save()
            palabra = palabraform.save(commit=False)
            palabra.tesis = tesis
            palabra.save()
    else:
        tesisform = TesisForm()
        autorform = AutorForm()
        evaluadorform = EvaluadorForm()
        palabraform = PalabraClaveForm()
    return render(request, 'tesisrmm/create.html', {'tesisform': tesisform, 'autorform': autorform,'evaluadorform': evaluadorform, 'palabraform': palabraform})
    
