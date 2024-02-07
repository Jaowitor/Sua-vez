from django.db import models

# Create your models here.
# Importações do Django
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
# Modelo do Usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    # Dados do Usuário.
    nome_usuario = models.CharField(_("Nome"), max_length=255)
    telefone_usuario = models.CharField(_("Telefone"), max_length=15)

    # Ver se o cliente foi atendido
    atendido = models.BooleanField(_("Atendido?"), default=False)

    # Dados de acesso e permissão
    atendido = models.BooleanField(_("Atendido?"), default=False)
    email_usuario = models.EmailField(_('E-mail'), unique=True, max_length=255)
    password = models.CharField(_("Senha"), max_length=255)
    is_staff = models.BooleanField(_("Administrador?"), default=False)
    is_active = models.BooleanField(_("Ativo?"), default=True)
    is_trusty = models.BooleanField(_('Verificado?'), default=True)
    date_joined = models.DateTimeField(_("Criação"), default=timezone.now)
    # Campo de Autenticação
    USERNAME_FIELD = 'email_usuario'
    # Gerenciador de operações de criação
    objects = UsuarioManager()

    def __str__(self):
        return self.nome_usuario
    
    class Meta:
        db_table = 'usuario'
        app_label = 'usuario'
