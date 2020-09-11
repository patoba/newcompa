from django.urls import path
from . import views

app_name = 'reuniones'
urlpatterns = [
    path('', views.reunion , name='reunion')
]