from xml.dom.minidom import Document

from django.urls import path
from .views import registrar, login, perfil, editar_perfil

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('salir/', LogoutView.as_view(template_name='accounts/salir.html') , name='salir'),
    path('perfil/', perfil, name='perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    ]


