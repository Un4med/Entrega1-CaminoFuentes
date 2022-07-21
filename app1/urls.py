from django.urls import path
from .views import crear_persona, vista, listado_persona
from . import views
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista, name='index'),
    path('crear-persona/', crear_persona, name='crear_persona'),
    path('persona/', listado_persona, name='listado_personas'),
    path('editar-persona/<int:pk>', views.EditarPersona.as_view(), name='editar_persona'),
    path('eliminar-persona/<int:pk>', views.EliminarPersona.as_view(), name='eliminar_persona'),
    path('mostrar-persona/<int:pk>', views.MostrarPersona.as_view(), name='mostrar_persona')
]
