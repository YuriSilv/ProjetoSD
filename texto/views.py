from django.shortcuts import render, redirect
from .models import Monografia
from .forms import MonografiaForm

# Create your views here.

def listar_monografias(request):
    monografias = Monografia.objects.all().order_by('titulo')
    return render(request, 'monografia.html', {'monografias': monografias})

def adicionar(request):
    if request.method == 'POST':
        form = MonografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'adicionar_monografia.html', {'form': form})
    else:
        form = MonografiaForm()
    
    return render(request, 'adicionar_monografia.html', {'form': form})