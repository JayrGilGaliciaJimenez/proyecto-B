from django import forms
from .models import Producto

INPUT_CLASSES = "form-control mt-2"


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su nombre de producto",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su precio de producto",
                }
            ),
            "imagen": forms.URLInput(attrs={"class": INPUT_CLASSES}),
        }

        labels = {
            "nombre": "Nombre del producto:",
            "precio": "Precio (MXN):",
            "imagen": "URL de la imagen:",
        }

        error_messages = {
            "precio": {
                "required": "El precio no puede estar vacio",
                "invalid": "Ingresa un precio valido",
            }
        }