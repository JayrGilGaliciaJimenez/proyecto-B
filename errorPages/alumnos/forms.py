from django import forms
from .models import Alumno

INPUT_CLASSES = "form-control mt-2"


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "apellido", "edad", "matricula", "correo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su nombre",
                }
            ),
            "apellido": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su apellido",
                }
            ),
            "edad": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su edad",
                }
            ),
            "matricula": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su matricula",
                }
            ),
            "correo": forms.EmailInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su correo",
                }
            ),

        }

        labels = {
            "nombre": "Nombre del producto:",
            "apellido": "Apellido",
            "edad": "Edad",
            "matricula": "Matricula",
            "correo": "Correo",
        }

        error_messages = {
            "nombre": {
                "required": "El nombre no puede estar vacio",
                "invalid": "Ingresa un nombre valido",
            },
            "apellido": {
                "required": "El apellido no puede estar vacio",
                "invalid": "Ingresa un apellido valido",
            },
            "edad": {
                "required": "La edad no puede estar vacio",
                "invalid": "Ingresa una edad valida",
            },
            "matricula": {
                "required": "La matricula no puede estar vacio",
                "invalid": "Ingresa una matricula valida",
            }
        }
