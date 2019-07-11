from django.http import HttpResponse
from django.shortcuts import render
from .forms import TesisForm, PalabraClaveForm, AutorForm, EvaluadorForm

def index(request):
    return render(request, 'tesisrmm/index.html')

def tesis(request):
    return render(request, 'tesisrmm/tesis.html')

def create(request):
    if request.method == "POST":
        tesisform = TesisForm(request.POST)
        if tesisform.is_valid():
            tesisform.save()
    else:
        tesisform = TesisForm()
    return render(request, 'tesisrmm/create.html', {'tesisform': tesisform},)
    
