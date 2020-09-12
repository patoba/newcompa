from django.shortcuts import render, redirect
<<<<<<< HEAD
#from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
=======
from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
>>>>>>> usuario

# Create your views here.
def registro(response):
    if response.method == "POST":
<<<<<<< HEAD
        form = UserCreationForm(response.POST)
=======
        form = RegisterForm(response.POST, response.FILES)
>>>>>>> usuario
        if form.is_valid():
            form.save()
            return redirect("/")
    else:        
        form = UserCreationForm()
    return render(response, "registration/registro.html", {"form":form})

def cuestionario(response):
    return render(response, "registration/cuestionario.html")

