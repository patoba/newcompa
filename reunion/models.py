from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from usuario.models import Usuario

class Lugar(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    altitud = models.DecimalField(max_digits=8,decimal_places=6)
    latitud = models.DecimalField(max_digits=8,decimal_places=6)
    imagen = models.ImageField()
    descripcion = models.TextField()
    nombre = models.CharField(max_length=255)

class Actividad(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField()
    descripcion = models.TextField()


class Reunion(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    fecha = models.DateTimeField()
    cantidad_personas = models.IntegerField()
    lugar_id = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    actividad_id = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    topico = models.CharField(max_length=255)

class UsuarioReunion(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    num_estrellas = models.IntegerField()
    comentario = models.TextField()
    reunion_id = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
