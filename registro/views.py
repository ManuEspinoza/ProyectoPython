from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import permission_required
from tesisrmm.views import index

@permission_required('auth.add_user')
def registrar(request):

    if request.method == "POST":
        userFrom = RegistrationForm(request.POST)
        if userFrom.is_valid():
            userFrom.save()
            usuario= User.objects.get(username=request.POST.get("username"))
            value = request.POST.get('rol', None)
            usuario.groups.add(value) 
            return redirect(index)        
    else:
        userFrom = RegistrationForm()
        
    


    return render(request, 'registro/registrar.html', {'userFrom': userFrom})
    
