from django.shortcuts import render
from .models import Monografia
# Create your views here.

def listar_monografias(request):
    monografias = Monografia.objects.all().order_by('titulo')
    return render(request, 'monografia.html', {'monografias': monografias})
