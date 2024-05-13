from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from equipe.models import Pesquisador
from texto.models import Monografia
from .serializers import PesquisadorSerializer, MonografiaSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def get_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)

    return JsonResponse({'token': token.key, 'user': user.username, 'password': user.password})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
    operation_description="Retorna todos os pesquisadores",
    responses={200: 'Success'},
    summary="Lista dos Usuários",
)
def get_data_pesquisador(request):
    pesquisador = Pesquisador.objects.all()
    serializer = PesquisadorSerializer(pesquisador, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Adiciona um Pesquisador",
    responses={200: 'Success'},
)
def add_data_pesquisador(request):
    serializer = PesquisadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@swagger_auto_schema(
    operation_description="Deleta um Pesquisador, dado um ID",
    responses={200: 'Success'},
)
def delete_data_pesquisador(request, id):
    try:
        pesquisador = Pesquisador.objects.get(id=id)
    except Pesquisador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pesquisador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@swagger_auto_schema(
    operation_description="Atualiza um pesquisador dado um ID",
    responses={200: 'Success'},
)
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




@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Retorna todos os textos",
    responses={200: 'Success'},
    summary="Lista dos textos",
)
def get_data_monografia(request):
    monografia = Monografia.objects.all()
    serializer = MonografiaSerializer(monografia, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Adiciona um Texto",
    responses={200: 'Success'},
)
def add_data_monografia(request):
    serializer = MonografiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@swagger_auto_schema(
    operation_description="Deleta uma Monografia, dado um ID",
    responses={200: 'Success'},
)
def delete_data_monografia(request, id):
    try:
        monografia = Monografia.objects.get(id=id)
    except Monografia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    monografia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@swagger_auto_schema(
    operation_description="Atualiza uma monografia, dado um ID",
    responses={200: 'Success'},
)
def update_data_monografia(request, id):
    try:
        monografia = Monografia.objects.get(id=id)
    except Monografia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MonografiaSerializer(monografia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)