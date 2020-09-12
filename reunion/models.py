from django.db import models
from usuario.models import Usuario
# Create your models here.

class Reunion(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    actividad = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    cantidad_personas = models.IntegerField()


class Feedback(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    numero_estrellas = models.IntegerField()
    comentarios = models.CharField(max_length=255)

class Usuaio_reunion(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Reunion_id = models.ForeignKey(Reunion, on_delete=models.CASCADE)