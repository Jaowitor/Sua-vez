# Importações do Django
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# nova branch
# Classe responsável pelo gerenciamento de criação de usuários e superusuários
class UsuarioManager(BaseUserManager):

    # Método para cadastrar um usuário
    # Cria e salva um novo usuário com o email e senha fornecidos.
    # **extra_fields permite fornecer campos adicionais para o usuário.
    def create_user(self, email_usuario, password, **extra_fields):
        if not email_usuario:
            # Lança um erro se o email não for fornecido
            raise ValueError(_('The Email must be set'))  
        email_usuario = self.normalize_email(email_usuario) # Verifica se o email é válido
        user = self.model(email_usuario=email_usuario, **extra_fields) # Cria uma instância de cliente do modelo de cliente com o email e campos extras fornecidos
        user.set_password(password) # Define e criptografa a senha do Cliente
        user.save() # Salva o Cliente no banco de dados
        return user


    # Método para cadastrar um superusuário
    def create_superuser(self, email_usuario, password, **extra_fields):
        extra_fields.setdefault('is_staff', True) # Define o campo is_staff como True (funcionário)
        extra_fields.setdefault('is_superuser', True) # Define o campo is_superuser como True (superusuário)
        extra_fields.setdefault('is_active', True) # Define o campo is_active como True (ativo)
        extra_fields.setdefault('is_trusty', True) # Define o campo is_trusty como True (confiável)

        if extra_fields.get('is_staff') is not True:
            # Lança um erro se is_staff não for True
            raise ValueError(_('Superuser must have is_staff=True.')) 
        if extra_fields.get('is_superuser') is not True:
            # Lança um erro se is_superuser não for True
            raise ValueError(_('Superuser must have is_superuser=True.')) 
        # Chama o método create_user para criar o superusuário
        return self.create_user(email_usuario, password, **extra_fields)  