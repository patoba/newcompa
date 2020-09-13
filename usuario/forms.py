from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Pregunta, Respuesta
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin


class RegisterForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ["nombre", "username", "genero", "correo", "facultad", "fecha_nacimiento", "credencial", "password1", "password2"]

class PreguntaForm(forms.ModelForm):
    def __init__(self, pregunta, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        self.fields['respuestas'] = forms.ModelChoiceField(
            queryset=Respuesta.objects.filter(pregunta=pregunta)
        )
    class Meta:
        model = Pregunta
        fields = ["texto"]
# admin.site.register(Usuario)
