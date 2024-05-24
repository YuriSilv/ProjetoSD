from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_view, name='dash_view'),
    # Adicione outras URLs conforme necessário
]
