import json

from django.shortcuts import render, redirect

from productos.models import Producto
from .models import Categoria
from django.http import JsonResponse

from .forms import categoriaForm


def lista_categorias(request):
    categorias = Categoria.objects.all()

    data = [
        {"nombre": p.nombre, "imagen": p.imagen} for p in categorias
    ]

    return JsonResponse(data, safe=False)


def ver_categorias(request):
    return render(request, "verCategorias.html")


def agregar_categoria(request):

    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid:
            form.save()
            #return redirect("ver")
    else:
        form = categoriaForm()
    return render(request, "agregarCategoria.html", {"form": form})

def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            ) # create mete el objeto directamente a la base de datos
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso!',
                    'id': categoria.id
                }, status=201

            )
        except Exception as e:
            print(e)
            return JsonResponse(
                {
                    'error': str(e)
                }, status=400
            )
    return JsonResponse(
        {'error': 'El metodo no esta soportado'},
        status=405
    )


