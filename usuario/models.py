from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model


GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'OTRO')
)

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length= 1, choices=GENDER_CHOICES)
    correo = models.EmailField(default="patobarrero@gmail.com")
    # otro_correo = models.EmailField()
    facultad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    credencial = models.ImageField()
    verificado = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

# Create your models here.

class Pregunta(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    texto = models.CharField(max_length=100)

class Respuesta(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    imagen = models.ImageField()

class Respuesta_Usuario(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    imagen = models.ImageField()

