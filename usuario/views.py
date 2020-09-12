from django.shortcuts import render, redirect
#from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registro(response):
    if response.method == "POST":
<<<<<<< .merge_file_ezHiV0
        form = RegisterForm(response.POST, response.FILES)
=======
        form = UserCreationForm(response.POST)
>>>>>>> .merge_file_wnkmDj
        if form.is_valid():
            form.save()
            return redirect("/")
    else:        
        form = UserCreationForm()
    return render(response, "registration/registro.html", {"form":form})

def cuestionario(response):
    return render(response, "registration/cuestionario.html")

