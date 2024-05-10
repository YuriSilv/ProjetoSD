from django.forms import ModelForm
from .models import Pesquisador

class EquipeForm(ModelForm):
    class Meta:
        model = Pesquisador
        fields = '__all__'