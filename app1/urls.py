from django.urls import path
from .views import crear_persona, vista, listado_persona, editar_persona, eliminar_persona, mostrar_persona
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista, name='index'),
    path('crear-persona/', crear_persona, name='crear_persona'),
    path('persona/', listado_persona, name='listado_personas'),
    path('editar-persona/<int:id>', editar_persona , name='editar_persona'),
    path('eliminar-persona/<int:id>', eliminar_persona, name='eliminar_persona'),
    path('mostrar-persona/<int:id>', mostrar_persona , name='mostrar_persona')
]
