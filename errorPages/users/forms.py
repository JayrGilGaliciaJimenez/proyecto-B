from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Contraseña',
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Confirmar contraseña',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Correo electrónico',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Nombre',
                    'maxlength': 30,
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Apellido',
                    'maxlength': 30,
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Número de control',
                    'maxlength': 10,
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Edad',
                    'min': 1,
                    'max': 120,
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Teléfono',
                    'maxlength': 10,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')
        control_number = cleaned_data.get('control_number')
        age = cleaned_data.get('age')
        tel = cleaned_data.get('tel')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if len(name) > 30:
            raise forms.ValidationError({'name': 'El nombre no puede tener más de 30 caracteres.'})
        
        if len(surname) > 30:
            raise forms.ValidationError({'surname': 'El apellido no puede tener más de 30 caracteres.'})
        
        if len(control_number) > 10:
            raise forms.ValidationError({'control_number': 'El número de control no puede tener más de 15 caracteres.'})
        
        if age < 1 or age > 120:
            raise forms.ValidationError({'age': 'La edad debe estar entre 1 y 120 años.'})
        
        if len(tel) > 10 or len(tel) < 10:
            raise forms.ValidationError({'tel': 'El teléfono debe tener exactamente 10 digitos.'})
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError({'password2': 'Las contraseñas no coinciden.'})


        if not email.endswith('@utez.edu.mx'):
            raise forms.ValidationError({'email': 'El correo debe ser de la UTEZ (@utez.edu.mx).'})

        if not re.match(r'^[0-9]{4}[1-3]{1}[a-zA-Z]{2}[0-9]{3}$', control_number):
            raise forms.ValidationError({'control_number': 'La matrícula debe ser de la UTEZ (ejemplo: 20223tn052).'})

        if not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError({'tel': 'El teléfono debe tener exactamente 10 dígitos.'})

        if password1 != password2:
            raise forms.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        
        if password2 != password1:
            raise forms.ValidationError({'password1': 'Las contraseñas no coinciden.'})

        if not re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            raise forms.ValidationError({'password1': 'La contraseña debe tener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial.'})

        return cleaned_data

class CustomUserLoginForm(AuthenticationForm):
    pass