from django.urls import path
from .views import crear_publicaciones, nosotros, vista, listado_publicaciones, editar_publicaciones, eliminar_publicaciones, mostrar_publicaciones
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('crear-publicacion/', crear_publicaciones, name='crear_publicacion'),
    path('publicaciones/', listado_publicaciones, name='listado_publicaciones'),
    path('editar-publicaciones/<int:id>', editar_publicaciones , name='editar_publicaciones'),
    path('eliminar-publicaciones/<int:id>', eliminar_publicaciones, name='eliminar_publicaciones'),
    path('mostrar-publicaciones/<int:id>', mostrar_publicaciones , name='mostrar_publicaciones'),
]
