from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pregunta(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    texto = models.CharField(max_length=100)
    
class Respuesta(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    imagen = models.ImageField()

class Pregunta_Respuesta_Usuario(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)