from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from .forms import AlumnoForm
from .models import Alumno
from .serializers import AlumnoSerializer



class AlumnoViewSet(viewsets.ModelViewSet):
    # esta variable nos dice de donde saca los datos para el modelo
    queryset = Alumno.objects.all()
    # serializar la informacion
    serializer_class = AlumnoSerializer
    # renderizar la informacion
    renderer_classes = [JSONRenderer]

    # Filtrar los metdos http que se pueden usar
    # si no se especifica se pueden usar todos
    # http_method_names = ['get', 'post', 'put']

def gestion_alumnos(request):
    form = AlumnoForm()
    return render(request, "galiciaJayr.html", {"form": form})