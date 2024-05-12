from rest_framework.response import Response #pega o dado e transforma em json
from rest_framework.decorators import api_view
from equipe.models import Pesquisador
from .serializers import PesquisadorSerializer
from rest_framework import status


@api_view(['GET'])
def get_data_pesquisador(request):
    pesquisador = Pesquisador.objects.all()
    serializer = PesquisadorSerializer(pesquisador, many=True)
    return Response(serializer.data) #recebe a info em dict e retorna o json


@api_view(['POST'])
def add_data_pesquisador(request):
    serializer = PesquisadorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_data_pesquisador(request, id):
    try:
        pesquisador = Pesquisador.objects.get(id=id)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pesquisador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_data_pesquisador(request, id):
    try:
        pesquisador = Pesquisador.objects.get(id=id)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PesquisadorSerializer(pesquisador, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
