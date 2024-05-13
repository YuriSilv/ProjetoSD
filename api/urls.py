from django.urls import path
from . import views

urlpatterns = [
    path('pesquisadores/', views.get_data_pesquisador, name='get_data_pesquisador'),
    path('pesquisadores/add/', views.add_data_pesquisador, name='add_data_pesquisador'),
    path('pesquisadores/update/<int:id>/', views.update_data_pesquisador, name='update_data_pesquisador'),
    path('pesquisadores/delete/<int:id>/', views.delete_data_pesquisador, name='delete_data_pesquisador'),
    path('', views.get_data_monografia, name='get_data_monografia'),
    path('monografias/add/', views.add_data_monografia, name='add_data_monografia'),
    path('monografias/update/<int:id>/', views.update_data_monografia, name='update_data_monografia'),
    path('monografias/delete/<int:id>/', views.delete_data_monografia, name='delete_data_monografia'),

]
