from rest_framework import serializers
from equipe.models import Pesquisador
from texto.models import Monografia

class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisador
        fields = '__all__'

class MonografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monografia
        fields = '__all__'