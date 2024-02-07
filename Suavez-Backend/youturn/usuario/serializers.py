# Importações do Django
from rest_framework import serializers

# Importações do Sistema
from .models import Usuario

# Usuário Serializador
class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Usuario

        fields = "id","password","email_usuario","telefone_usuario",

    #criação do usuario
    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)
    
    # Atualização de Usuário
    def update(self, instance, validated_data):
        usuario = super().update(instance, validated_data)

        try:

            usuario.set_password(validated_data['password'])
            usuario.save()

        except KeyError:

            pass

        return usuario
