from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model


GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'OTRO')
)

FACULTY_CHOICES = (
        ('FI', 'Facultad de Ingeniería'),
        ('FC', 'Facultad de Ciencias'),
        ('FCA', 'Facultad de Contaduría y Administración'),
        ('FO', 'Facultad de Odontología'),
        ('FA', 'Facultad de Arquitectura'),
        ('FAD', 'Facultad de Artes y Diseño'),
        ('FQ', 'Facultad de Química'),
        ('FD','Facultad de Derecho'),
        ('FCPS', 'Facultad de Ciencias Políticas y Sociales'),
        ('FM','Facultad de Medicina'),
        ('FE', 'Facultad de Economía'),
        ('FMVZ','Facultad de Medicina Veterinaria y Zootecnia'),
        ('FP','Facultad de Psicología'),
        ('FFL', 'Facultad de Filosofía y Letras'),
)

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length= 1, choices=GENDER_CHOICES)
    correo = models.EmailField()
    # otro_correo = models.EmailField()
    facultad = models.CharField(max_length=4, choices=FACULTY_CHOICES)
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

