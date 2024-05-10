from django.forms import ModelForm
from .models import Monografia

class MonografiaForm(ModelForm):
    class Meta:
        model = Monografia
        fields = '__all__'