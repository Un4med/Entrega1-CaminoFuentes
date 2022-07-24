from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from grupos.models import Dios

# Create your views here.
class ListadoDioses(ListView):
    model= Dios
    template_name = 'dioses/listado_dioses.html'
    

class CrearDios(CreateView):
    model= Dios
    template_name = 'dioses/crear_dios.html' 
    success_url= '/dioses/dios'
    fields= ['dios', 'edad', 'fecha_creacion']


class EditarDios(LoginRequiredMixin, UpdateView):
    model= Dios
    template_name = 'dioses/editar_dios.html'
    success_url= '/dioses/dios'
    fields= ['dios', 'edad', 'fecha_creacion']
    
    
class EliminarDios(LoginRequiredMixin, DeleteView):
    model= Dios
    template_name = 'dioses/eliminar_dios.html'
    success_url= '/dioses/dios'
    
    
class MostrarDios(DetailView):
     model= Dios
     template_name = 'dioses/mostrar_dios.html'