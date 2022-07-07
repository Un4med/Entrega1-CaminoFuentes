from django.shortcuts import redirect, render

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