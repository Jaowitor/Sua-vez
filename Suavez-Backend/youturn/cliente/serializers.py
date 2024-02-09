# serializers.py
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = "__all__"

class FilaCliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["nome_cliente","forma_identificacao",]