from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from .forms import productoForm
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # esta variable nos dice de donde saca los datos para el modelo
    queryset = Producto.objects.all()
    # serializar la informacion
    serializer_class = ProductoSerializer
    # renderizar la informacion
    renderer_classes = [JSONRenderer]

    # Filtrar los metdos http que se pueden usar
    # si no se especifica se pueden usar todos
    # http_method_names = ['get', 'post', 'put']

def agregar_producto(request):
    form = productoForm()
    return render(request, "agregar.html", {"form": form})