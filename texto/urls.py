from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_monografias, name='listar_monografias'),
    path('adicionar/', views.adicionar, name='adicionar_monografia'),
    path('editar/<int:id>/', views.editar_monografia, name='editar_monografia'),
    path('deletar/<int:id>/', views.deletar_monografia, name='deletar_monografia'),  
]
