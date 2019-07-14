from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm



def create(request):

    if request.method == "POST":
        userFrom = RegistrationForm(request.POST)
        #grupo_gerente = Group.objects.get(name = "Gerente")
        #usuario= User.objects.get(username=request.POST.get("username"))
        #usuario.groups.add(grupo_gerente)
        #grupo_usuario = Group.objects.get(name = "Usuario")

        if userFrom.is_valid():
            userFrom.save()
    else:
        userFrom = RegistrationForm()

    return render(request, 'registro/registrar.html', {'userFrom': userFrom})
    
