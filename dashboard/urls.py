from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dash_view, name='dash_view'),
    # Adicione outras URLs conforme necessário
]
