from django import forms
from .models import Categoria

INPUT_CLASSES = "form-control mt-2"


class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese el nombre de la categoria",
                }
            ),
            
            "imagen": forms.URLInput(attrs={"class": INPUT_CLASSES}),
        }

        labels = {
            "nombre": "Nombre de la categoria:",
            "imagen": "URL de la imagen:",
        }

        # error_messages = {
        #     "precio": {
        #         "required": "El precio no puede estar vacio",
        #         "invalid": "Ingresa un precio valido",
        #     }
        # }