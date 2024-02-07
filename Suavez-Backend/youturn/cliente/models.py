from django.db import models

# Create your models here.
# Importações do Django
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Cliente(models.Model):
    nome_cliente = models.CharField(_("Nome do Cliente"), max_length=255)
    forma_identificacao = models.CharField(_("Forma de Identificação"), max_length=255, blank=True, null=True)
    data_registro = models.DateTimeField(_("Data de Registro"), auto_now_add=True)

    class Meta:
        db_table = "cliente"
        app_label = "cliente"

    def __str__(self):
        return self.nome_cliente
