from django.urls import path
from .views import vista, mi_lista
#poner el INDEX HTML EN EL PATH VACIO

urlpatterns = [
    path('', vista),
    path('mi-lista/', mi_lista),
]
