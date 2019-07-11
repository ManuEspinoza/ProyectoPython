from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.tesis, name='tesis'),
    path('create/', views.create, name='tesis_new'),
]