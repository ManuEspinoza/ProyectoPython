from django.http import HttpResponse
from django.shortcuts import render
from .forms import TesisForm, PalabraClaveForm, AutorForm, EvaluadorForm, BuscadorForm
from .models import Tesis, Autor, Evaluador, PalabraClave
from django.contrib.auth.decorators import permission_required, login_required

@login_required
def index(request):
    print(request.user.get_group_permissions())
    if request.method == "POST":
        palabra = request.POST.get('palabra')
        tesis = [i for i in Tesis.objects.filter(nombre__icontains=palabra)]
        tesis = tesis + [i.aut_tesis for i in Autor.objects.filter(aut_nombre__icontains=palabra)]
        tesis = tesis + [i.eva_tesis for i in Evaluador.objects.filter(eva_nombre__icontains=palabra)]
        tesis = tesis + [i.tesis for i in PalabraClave.objects.filter(palabra__icontains=palabra)]
        tesis = list(set(tesis))
        buscadorform = BuscadorForm()
    else:
        user = request.user
        buscadorform = BuscadorForm()
        tesis = Tesis.objects.all().order_by('-id')[:6]
    return render(request, 'tesisrmm/inicio.html', {'tesis': tesis, 'buscadorform': buscadorform,'user':user})


@permission_required('tesisrmm.add_tesis')
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
    
def prueba(request):
    buscador = BuscadorForm()
    return render(request, 'tesisrmm/prueba.html',{'buscadorform': buscador})