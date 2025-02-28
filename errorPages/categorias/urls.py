from django.urls import path
from .views import *

urlpatterns = [
    path("api/get/", lista_categorias, name="lista"),
    path("ver/", ver_categorias, name="ver"),
    path("agregar/", agregar_categoria, name="agregar"),
    path("registrar/", registrar_categoria, name="registrar")

]

# https://cdn.shopify.com/s/files/1/2710/8782/files/4_fc54854c-7fde-400f-8751-4cfae6583045.jpg?v=1683378579