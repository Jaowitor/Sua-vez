from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import response, status, generics
from rest_framework.permissions import IsAuthenticated

# Importações do Sistema
from .models import Cliente
from .serializers import ClienteSerializer, FilaCliente

# Método GET
class ClinteList(generics.ListAPIView):
    
    # Se o cliente for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos de cliente do banco de dados
    queryset = Cliente.objects.all()

    # Utiliza o serializer clienteSerializer para serializar os objetos
    serializer_class = ClienteSerializer

    def get(self, request):

        # Pega todos os cliente 
        cliente_serializer = self.serializer_class(self.queryset.all(), many=True)

        # Retorna uma resposta com status HTTP 200 OK
        return response.Response(data=cliente_serializer.data, status=status.HTTP_200_OK)
    
# Método DETAIL
class ClinteDetail(generics.RetrieveAPIView):
    
    # Se o cliente for autenticado ele terá acesso ao método
    permission_classes = (IsAuthenticated, )
    
    # Obtém todos os objetos Cliente do banco de dados
    queryset = Cliente.objects.all() 

    # Utiliza o serializer ClienteSerializer para serializar os objetos
    serializer_class = ClienteSerializer

    def get(self, request, pk):

        try:

            # Pega um cliente com base nos dados enviados na solicitação
            cliente_serializer = self.serializer_class(self.queryset.get(pk=pk), many=False)
            
            # Retorna uma resposta com status HTTP 200 OK
            return response.Response(data = cliente_serializer.data, status = status.HTTP_200_OK)

        except:

            # Retorna uma resposta com status HTTP 200 OK
            return response.Response(data="Essa cliente não existe", status=status.HTTP_200_OK)
    

class ClienteCreate(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
def post(self, request):
    cliente_serializer = self.serializer_class(data=request.data)
    if cliente_serializer.is_valid():
        cliente_serializer.save()
        return response.Response(data=cliente_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return response.Response(data=cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Método put
class ClienteUpdate(generics.RetrieveUpdateAPIView):

    # Se o usuário for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos Usuário do banco de dados
    queryset = Cliente.objects.all()

    # Utiliza o serializer UsuárioSerializer para serializar os objetos
    serializer_class = ClienteSerializer

    def put(self, request, pk):

        # Recupera o cliente com o ID fornecido (pk)
        usuario = self.queryset.get(pk=pk)

        # Atualiza seus dados com base nos dados enviados na solicitação
        cliente_serializer = self.serializer_class(usuario, data=request.data)

        # Se o usuário estiver válido
        if cliente_serializer.is_valid():

            # Salva o cliente no banco de dados
            cliente_serializer.save()

            # Retorna uma resposta com status HTTP 200 OK
            return response.Response(data=cliente_serializer.data, status=status.HTTP_200_OK)
        
        else:
            # Retorna uma resposta com status HTTP 400 Bad Request caso os dados enviados sejam inválidos
            return response.Response(data=cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Método DELETE
class ClienteDelete(generics.RetrieveDestroyAPIView):
    
    # Se o cliente for autenticado ele terá acesso ao método
    permission_classes = [IsAuthenticated]

    # Obtém todos os objetos cliente do banco de dados
    queryset = Cliente.objects.all()

    # Utiliza o serializer ClienteSerializer para serializar os objetos
    serializer_class = ClienteSerializer

    def delete(self, request, pk):

        # Recupera o cliente com o ID fornecido (pk)s
        cliente = self.queryset.get(pk=pk)

        # Exclui o cliente recuperado do banco de dados        
        cliente.delete()

        # Retorna uma resposta vazia com status HTTP 204 No Content para indicar que o cliente foi excluído com sucesso
        return response.Response(data=(), status=status.HTTP_204_NO_CONTENT)