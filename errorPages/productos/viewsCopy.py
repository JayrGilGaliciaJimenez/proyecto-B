import json

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.http import JsonResponse

from .forms import productoForm


def lista_productos(request):
    productos = Producto.objects.all()

    data = [
        {"id": p.id, "nombre": p.nombre, "precio": p.precio, "imagen": p.imagen} for p in productos
    ]

    return JsonResponse(data, safe=False)


def ver_productos(request):
    return render(request, "ver.html")


def agregar_producto(request):

    if request.method == "POST":
        form = productoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("ver")
    else:
        form = productoForm()
    return render(request, "agregar.html", {"form": form})

def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            ) # create mete el objeto directamente a la base de datos
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso!',
                    'id': producto.id
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

# Funciones para ael metodo PUT


def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto, id=id_producto)
        try:
            # La informacion del al modificacion del producto viene del body
            data = json.loads(request.body)
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse(
                {
                    'mensaje': 'Producto actualizado correctamente'
                }, status=200
            )
        except Exception as e:
            return JsonResponse(
                {
                    'error': str(e)
                }, status=400
            )
    return JsonResponse(
        {
            'error': 'El metodo no esta soportado'
        }, status=405
    )

#Funciones para el metodo DELETE

def borrar_producto(request, id_producto):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete() #Borra fisicamente el objeto de la base de datos
        return JsonResponse(
            {
                'mensaje': 'Producto eliminado correctamente'
            }, status=200
        )
    return JsonResponse(
        {
            'error': 'El metodo no esta soportado'
        }, status=405
    )


#Funcion para el metdo GET by ID

def obtener_producto(request, id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        return JsonResponse(
            {
                'nombre': producto.nombre,
                'precio': producto.precio,
                'imagen': producto.imagen
            }, status=200
        )
    return JsonResponse(
        {
            'error': 'El metodo no esta soportado'
        }, status=405
    )
