from django.shortcuts import render
from .models import Pesquisador

# Create your views here.
def listar_equipe(request):
    pesquisadores = Pesquisador.objects.all() #modelo do BD sobre a tabela pesquisador
    return render(request, 'equipe.html', {'pesquisadores': pesquisadores})
