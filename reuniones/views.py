from django.shortcuts import render

# Create your views here.
def reunion(request):
    return render(request, 'reuniones/reunion.html')