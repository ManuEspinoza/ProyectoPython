from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'tesisrmm/index.html')

def tesis(request):
    return render(request, 'tesisrmm/tesis.html')
