from django.shortcuts import render, redirect
from .models import Monografia
from .forms import MonografiaForm
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def listar_monografias(request):
    monografias = Monografia.objects.all().order_by('titulo')
    return render(request, 'monografia.html', {'monografias': monografias})

def adicionar(request):
    if request.method == 'POST':
        form = MonografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_monografias')
    else:
        form = MonografiaForm()
    
    return render(request, 'adicionar_monografia.html', {'form': form})


def editar_monografia(request, id):
    monografia = get_object_or_404(Monografia, id=id)

    if request.method == 'POST':
        form = MonografiaForm(request.POST, request.FILES, instance=monografia)
        if form.is_valid():
            form.save()
            return redirect('listar_monografias')  # Redirecionar para a lista de monografias após a edição
    else:
        form = MonografiaForm()

    return render(request, 'editar_monografia.html', {'form': form, 'monografia': monografia})


def deletar_monografia(request, id):
    monografia = get_object_or_404(Monografia, id=id)
    if request.method == 'POST':
        monografia.delete()
        return redirect('listar_monografias') 
    return render(request, 'deletar_monografia.html', {'monografia': monografia})

