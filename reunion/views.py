from django.shortcuts import render

# Create your views here.
def seleccionar_reunion(request):
    return render(request, 'reunion/seleccionar_reunion.html')

def detalle_reunion(request):
    return render(request, 'reunion/detalles_reunion.html')

def feedback(request):
    return render(request, 'reunion/feedback.html')

def crear_reunion(request):
    return render(request, 'reunion/crear_reunion.html')

def historial_reuniones(request):
    return render(request, 'reunion/historial_reuniones.html')