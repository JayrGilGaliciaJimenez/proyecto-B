from django.db import models
from categorias.models import Categoria
# Create your models here.

class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300),
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nomnre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    # primer paramatre es el modelo a relacionar y el segundo es la estrategia de eliminacion
    detalles_producto = models.OneToOneField(DetallesProducto, null=True, blank=True, on_delete=models.CASCADE)
    proveedor = models.ManyToManyField(Proveedor)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    # Cuando se requiera crear una relacion se usa un campo:
    # OneToOneField, ForeignKey, ManyToManyField


    def __str__(self):
        return self.nombre

    #Creamos una funcion que devuelva el objeto en fomma de diccionario o Dic
    def to_dict(self):
        return {
            # clave: valor
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
