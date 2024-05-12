from rest_framework import serializers
from equipe.models import Pesquisador

class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisador
        fields = '__all__'