from django.db import models

# Create your models here.

class Pregunta(models.Model):
<<<<<<< Updated upstream
    pass

class Respuesta(models.Model):
    pass
=======
    id = models.IntegerField(auto_created=True, primary_key=True)
    texto = models.CharField(max_length=100)

    def __str__(self):
        return "Pregunta {}: ¿{}?".format(id, texto)
    
class Respuesta(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=100)
    imagen = models.ImageField()
>>>>>>> Stashed changes

    def __str__(self):
        return "Respuesta {}: ¿{}?".format(id, texto)

class Pregunta_Respuesta_Usuario(models.Model):
<<<<<<< Updated upstream
    pass
=======
    id = models.IntegerField(auto_created=True, primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return "Respuesta {} de la pregunta {} del usuario {}".format(respuesta, pregunta, usuario)

>>>>>>> Stashed changes
