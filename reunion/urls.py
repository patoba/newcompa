from django.urls import path
from . import views

app_name = 'reunion'
urlpatterns = [
    path('seleccionar-reunion', views.seleccionar_reunion, name='seleccionar-reunion'), 
    path('detalle-reunion', views.detalle_reunion, name='detalle-reunion'),
    path('feedback', views.feedback, name='feedback'),
    path('crear-reunion', views.crear_reunion, name='crear-reunion'),
    path('historial-reuniones', views.historial_reuniones, name='historial-reuniones')
]