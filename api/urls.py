from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data_pesquisador, name='get_data_pesquisador'),
    path('add/', views.add_data_pesquisador, name='add_data_pesquisador'),
    path('update/', views.add_data_pesquisador, name='update_data_pesquisador'),
    path('delete/', views.add_data_pesquisador, name='delete_data_pesquisador'),
]
