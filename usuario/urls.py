from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('cuestionario', views.cuestionario, name = 'cuestionario')
]