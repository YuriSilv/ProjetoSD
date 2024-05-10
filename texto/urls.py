from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_monografias, name='listar_monografias'),
    path('adicionar/', views.adicionar, name='adicionar_monografia'),      
]
