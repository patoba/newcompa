from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

class RegisterForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ["nombre", "username", "genero", "correo", "facultad", "fecha_nacimiento", "credencial", "password1", "password2"]

# Admin
"""
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = RegisterForm
    model = Usuario
    list_display = ['email', 'username',]
"""
# admin.site.register(Usuario)
