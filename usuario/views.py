from django.shortcuts import render, redirect
from .forms import RegisterForm, PreguntaForm
from .models import Pregunta
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registro(response):
    if response.method == "POST":
        form = RegisterForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:        
        form = RegisterForm()
    return render(response, "registration/registro.html", {"form":form})

def cuestionario(response):
    preguntas = Pregunta.objects.all()
    cuestionario = [PreguntaForm(pregunta) for pregunta in preguntas]
    return render(response, "registration/cuestionario.html", {"forms":cuestionario})

