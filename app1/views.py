from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import DetailView

from .forms import BusquedaPersona, FormPersona
from .models import Persona
from datetime import datetime


# Create your views here.
def vista(request):
    return render(request, 'index.html')


def crear_persona(request):
    
    
    print(request.POST)
    
    if request.method =="POST":
        form= FormPersona(request.POST)
        if form.is_valid():
            data= form.cleaned_data 
            fecha= data.get('fecha_creacion')
            
            persona= Persona(
                nombre=data.get('nombre'), 
                edad=data.get('edad'), 
                fecha_creacion= fecha if fecha else datetime.now() )
            persona.save()
            
            listado_personas = Persona.objects.all()
            return redirect('listado_personas')
        
        else:
            return render(request, 'crear_persona.html', {form})   
        
    form_persona= FormPersona()
    
    return render(request, 'crear_persona.html', {'form': form_persona})


def listado_persona(request):
    nombre_de_persona= request.GET.get('nombre')
    
    if nombre_de_persona: 
        listado_personas= Persona.objects.filter(nombre__icontains= nombre_de_persona)
    else:
        listado_personas= Persona.objects.all()
    
    form= BusquedaPersona()
    return render(request, 'listado_personas.html', {'listado_personas': listado_personas,'form': form})


class EditarPersona(UpdateView):
    model: Persona
    template_name = 'editar_persona.html'
    success_url= "listado_personas"
    fields= ['nombre', 'edad', 'fecha_creacion']


class EliminarPersona(DeleteView):
    model: Persona
    template_name = 'eliminar_persona.html'
    success_url= "listado_personas"


class MostrarPersona(DetailView):
    model: Persona
    template_name = 'mostrar_persona.html'
    success_url= "listado_personas"