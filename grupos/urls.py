from django.urls import path
from . import views

urlpatterns = [
    path('crear-dios/', views.CrearDios.as_view(), name='crear_dios'),
    path('dios/',views.ListadoDioses.as_view() , name='listado_dioses'),
    path('editar-dios/<int:pk>', views.EditarDios.as_view() , name='editar_dios'),
    path('eliminar-dios/<int:pk>',views.EliminarDios.as_view() , name='eliminar_dios'),
    path('mostrar-dios/<int:pk>', views.MostrarDios.as_view() , name='mostrar_dios')
]
