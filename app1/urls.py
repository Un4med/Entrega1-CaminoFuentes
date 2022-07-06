from django.urls import path
from .views import crear_persona, vista
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista, name='index'),
    path('crear-persona/', crear_persona, name='crear_persona'),
]
