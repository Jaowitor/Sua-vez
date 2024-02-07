from django.urls import path
from .views import *

urlpatterns = [
    path("", UsuarioList.as_view(), name="usuario-list"),
    path("create/", UsuarioCreate.as_view(), name="usuario-create"),
    path('update/<int:pk>/', UsuarioUpdate.as_view(), name="usuario-update"),
    path('delete/<int:pk>/', UsuarioDelete.as_view(), name="Usuario-delete"),

]
