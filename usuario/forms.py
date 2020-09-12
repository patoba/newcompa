from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
class RegisterForm(UserCreationForm):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    correo_unam = forms.EmailField()
    otro_correo = forms.EmailField()
    facultad = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()
    credencial = models.ImageField()

    class Meta:
        model = User
        fields = ["nombre", "username", "genero", "correo_unam", "otro_correo", "facultad", "fecha_nacimiento", "credencial", "password1", "password2"]
