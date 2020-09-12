from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Usuario,Pregunta
# Register your models here.

class UsuarioAdmin(UserAdmin):
    list_display = ('nombre', 'genero', 'correo')

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto',)


# admin.site.unregister(Usuario)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)