from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=11)
    correo = models.EmailField()


    def __str__(self):
        return self.nombre

    # Creamos una funcion que devuelva el objeto en forma de diccionario o Dic
    def to_dict(self):
        return {
            # clave: valor
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }

