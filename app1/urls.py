from django.urls import path
from .views import crear_persona, vista, listado_persona
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista, name='index'),
    path('crear-persona/', crear_persona, name='crear_persona'),
    path('persona/', listado_persona, name='listado_personas'),
]
