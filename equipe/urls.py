from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipe, name='listar_equipe'),    
]
