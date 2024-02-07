from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import response, status, generics
from rest_framework.permissions import IsAuthenticated

# Importações do Sistema
from .models import Usuario
from .serializers import UsuarioSerializer


# Método GET
class UsuarioList(generics.ListAPIView):

    # Se o usuário for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos de usuário do banco de dados
    queryset = Usuario.objects.all()

    # Utiliza o serializer usuárioSerializer para serializar os objetos
    serializer_class = UsuarioSerializer

    def get(self, request):

        # Pega todos os usuário 
        user_serializer = self.serializer_class(self.queryset.all(), many=True)

        # Retorna uma resposta com status HTTP 200 OK
        return response.Response(data=user_serializer.data, status=status.HTTP_200_OK)
class UsuarioCreate(generics.CreateAPIView):

    # Se o usuário for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Pega todos os objectos de Usuario
    queryset = Usuario.objects.all()

    # Utiliza o serializer usuárioSerializer para serializar os objetos
    serializer_class = UsuarioSerializer

    def post(self, request):

        #Cria um novo usuário com base nos dados enviados na solicitação
        user_serializer = self.serializer_class(data=request.data)

        # Verifica se o usuário está válido
        if user_serializer.is_valid():

            # Salva no banco de dados 
            user_serializer.save()
            # Retorna uma resposta com status HTTP 201 Created
            return response.Response(data=user_serializer.data, status=status.HTTP_201_CREATED)
        
        else:

            # Retorna uma resposta com status HTTP 400 Bad Request caso os dados enviados sejam inválidos
            return response.Response(data=user_serializer.errors, status=status.HTTP_BAD_REQUEST)
# Método put
class UsuarioUpdate(generics.RetrieveUpdateAPIView):

    # Se o usuário for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos Usuário do banco de dados
    queryset = Usuario.objects.all()

    # Utiliza o serializer UsuárioSerializer para serializar os objetos
    serializer_class = UsuarioSerializer

    def put(self, request, pk):

        # Recupera o usuário com o ID fornecido (pk)
        usuario = self.queryset.get(pk=pk)

        # Atualiza seus dados com base nos dados enviados na solicitação
        user_serializer = self.serializer_class(usuario, data=request.data)

        # Se o usuário estiver válido
        if user_serializer.is_valid():

            # Salva o usuário no banco de dados
            user_serializer.save()

            # Retorna uma resposta com status HTTP 200 OK
            return response.Response(data=user_serializer.data, status=status.HTTP_200_OK)
        
        else:
            # Retorna uma resposta com status HTTP 400 Bad Request caso os dados enviados sejam inválidos
            return response.Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Método DELETE
class UsuarioDelete(generics.RetrieveDestroyAPIView):
    
    # Se o usuário for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos Usuario do banco de dados
    queryset = Usuario.objects.all()

    # Utiliza o serializer UsuarioSerializer para serializar os objetos
    serializer_class = UsuarioSerializer

    def delete(self, request, pk):

        # Recupera o usuário com o ID fornecido (pk)s
        usuario = self.queryset.get(pk=pk)

        # Exclui o usuário recuperado do banco de dados        
        usuario.delete()

        # Retorna uma resposta vazia com status HTTP 204 No Content para indicar que o usuário foi excluído com sucesso
        return response.Response(data=(), status=status.HTTP_204_NO_CONTENT)