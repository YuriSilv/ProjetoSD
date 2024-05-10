from django.shortcuts import render
from .models import Pesquisador
from .forms import EquipeForm

# Create your views here.
def listar_equipe(request):
    pesquisadores = Pesquisador.objects.all() #modelo do BD sobre a tabela pesquisador
    return render(request, 'equipe.html', {'pesquisadores': pesquisadores})

def adicionar(request):
    form = EquipeForm(request.POST)
    if request.method == 'POST':
        form = EquipeForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.save()
            form = EquipeForm()
            return render(request, 'adicionar_equipe.html', {'form': form})

        form = EquipeForm()
        
    return render(request, 'adicionar_equipe.html', {'form': form})