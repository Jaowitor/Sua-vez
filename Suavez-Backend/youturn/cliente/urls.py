from django.urls import path
from .views import *

urlpatterns = [
    path("", ClinteList.as_view(), name="usuario-list"),
    path('<int:pk>/', ClinteDetail.as_view(), name="cliente-detail"),


    path("create/", ClienteCreate.as_view(), name="usuario-create"),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name="usuario-update"),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name="Usuario-delete"),

]
